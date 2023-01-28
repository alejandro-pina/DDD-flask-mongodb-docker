from app.auth import auth
from flask import request, make_response
from app.auth.infractucture.routes.const.auth_public_routes import ep_auth_public_routes
from app.auth.infractucture.dtos.login_user__dto import LoginUserDTO
from app.auth.infractucture.controllers.auth__controller import AuthController
from app.services.processors import process_request
from app.auth.infractucture.errors.auth__error import auth_infractuture_error_message


epa_login = ep_auth_public_routes('epa_login')
@auth.route(epa_login['endpoint'], methods=epa_login['methods'])
@process_request(request, get_rq=['data'], content_type='application/json')
def login(rq_info):

    data     = rq_info['data']
    email    = data['email']
    password = data['password']
    
    if email == '' or password == '': 
        return auth_infractuture_error_message('auth_data'), 400

    dto_input  = LoginUserDTO(
        email    = email,
        password = password
    )

    try:
        auth_login = AuthController(dto_input).execute()
    except:
        return auth_infractuture_error_message('login'), 444

    if 'error' in auth_login: return auth_login, 400

    if 'tka' in auth_login:
        tka  = auth_login['tka']
        resp = make_response(auth_login)
        resp.set_cookie('x-tka',tka, httponly = True)
        resp.headers['x-tka'] = tka
        return resp

    return auth_infractuture_error_message('login'), 444