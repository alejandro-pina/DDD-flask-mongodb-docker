from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, decode_token
from functools import wraps
from datetime import datetime, timezone
from .mongodb.black_list__mongodb import Blacklist


def get_expires(tk: str) -> int:
    # Decode the JWT and get the payload as a dictionary
    payload = decode_token(tk)
    # Get the expiry time of the refresh token
    exp_timestamp = payload['exp']
    exp_datetime = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
    # Get the current time
    now = datetime.now(timezone.utc)
    time_remaining = (exp_datetime - now).total_seconds()
    return time_remaining


def add_black_list(tk: str) -> bool:
    ttl = get_expires(tk)
    return Blacklist.add({'token': tk}, ttl)


def is_connection_valid(tk: str) -> bool:
    token_in_black_list = Blacklist.is_blacklisted({'token': tk})
    if token_in_black_list:
        return False
    return True


class AuthService():

    def signin(id_: str) -> dict:
        access_token = create_access_token(identity=id_, fresh=True)
        return {
            'tka': access_token
        }

    def logout(tk: str) -> dict:
        try:
            add_black_list(tk)
            return {
                'msg': 'Logout successful.'
            }
        except:
            return {
                'error': 'Cant logout action.'
            }

    def auth_connection(request, fresh=False):
        def decorator(f):
            @wraps(f)
            @jwt_required(fresh=fresh)
            def wrapper(*args, **kwargs):
                current_user = {}
                current_user['id'] = get_jwt_identity()
                current_user['tk'] = request.headers.get('Authorization').split()[1]
                if not is_connection_valid(current_user['tk']):
                    return {'error': 'Session expired, login again to continue.'}, 403
                return f(current_user, *args, **kwargs)
            return wrapper
        return decorator
