from app.auth import auth 
from flask import request
from app.services.auth__service import AuthService
from app.auth.infractucture.routes.const.auth_private_routes import ep_auth_private_routes
from app.auth.infractucture.errors.auth__error import auth_infractuture_error_message

epa_auth = ep_auth_private_routes('epa_auth')
@auth.route(epa_auth['endpoint'], methods=epa_auth['methods'])
@AuthService.auth_connection(request, fresh=False)
def auth_wellcome(current_user):
    return '🛰 API AUTH'

epa_logout = ep_auth_private_routes('epa_logout')
@auth.route(epa_logout['endpoint'], methods=epa_logout['methods'])
@AuthService.auth_connection(request, fresh=False)
def logout(current_user):
    tk = current_user['tk']
    if tk == '': return auth_infractuture_error_message('logout'), 400
    try:
        return AuthService.logout(tk)
    except:
        return auth_infractuture_error_message('logout'), 444