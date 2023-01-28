from app.api import api
from flask import request
from app.services.auth__service import AuthService
from app.api.user.infractucture.routes.const.user__private_routes import ep_user_private_routes
from app.api.user.infractucture.dtos.get_users_input__dto import GetUsersInputDTO
from app.api.user.infractucture.controllers.get_users__controller import GetUsersController
from app.api.user.infractucture.controllers.get_user_by_email__controller import GetUserByEmailController
from app.api.user.infractucture.dtos.register_user__dto import CreateUserDTO
from app.api.user.infractucture.controllers.create_user__controller import CreateUserController
from app.api.user.infractucture.dtos.update_user__dto import UpdateUserDTO
from app.api.user.infractucture.controllers.update_user__controller import UpdateUserController
from app.api.user.infractucture.controllers.delete_user__controller import DeleteUserController
from app.services.order_by_insert_JSON__libs import order_by_insert_JSON
from app.services.processors import process_request
from app.api.user.infractucture.errors.user__error import infractuture_user_error_message

ep_get_user_profile = ep_user_private_routes('ep_get_user_profile')


@api.route(ep_get_user_profile['endpoint'], methods=ep_get_user_profile['methods'])
@AuthService.auth_connection(request, fresh=False)
@process_request(request, get_rq=['path', 'data'], content_type='application/json')
def get_user_profile(rq_info, current_user):
    return {
        'msg': 'Wellcome user: ' + current_user['id']
    }


ep_get_users = ep_user_private_routes('ep_get_users')


@api.route(ep_get_users['endpoint'], methods=ep_get_users['methods'])
@AuthService.auth_connection(request, fresh=False)
@process_request(request, get_rq=['path', 'data'], content_type='application/json')
def get_users(rq_info, current_user):
    path = rq_info['path']
    data = rq_info['data']
    try:
        dto_input = GetUsersInputDTO(
            page       = data.get('page'),
            per_page   = data.get('per_page'),
            sort_field = data.get('sort_field'),
            order_by   = data.get('order_by'),
            endpoint   = path,
        )
        list_users = GetUsersController(dto_input).execute()
        if 'error' in list_users:
            return list_users, 404
        return order_by_insert_JSON(list_users)
    except:
        return infractuture_user_error_message('users'), 400


ep_get_user_by_email = ep_user_private_routes('ep_get_user_by_email')


@api.route(ep_get_user_by_email['endpoint'], methods=ep_get_user_by_email['methods'])
@AuthService.auth_connection(request, fresh=False)
@process_request(request, get_rq=['data'], content_type='application/json')
def search_user_by_emai(rq_info, current_user):

    data = rq_info['data']

    if not 'email' in data:
        return infractuture_user_error_message('user_data'), 400

    try:
        email = data.get('email')
        find_user_by_email = GetUserByEmailController(email).execute()
        if 'error' in find_user_by_email:
            return find_user_by_email, 404
        return order_by_insert_JSON(find_user_by_email)
    except:
        return infractuture_user_error_message('email'), 400


ep_create_user = ep_user_private_routes('ep_create_user')


@api.route(ep_create_user['endpoint'], methods=ep_create_user['methods'])
@AuthService.auth_connection(request, fresh=False)
@process_request(request, get_rq=['data'], content_type='application/json')
def create_user(rq_info, current_user):

    data = rq_info['data']

    if not 'name' in data or data.get('name', '') == '':
        return infractuture_user_error_message('user_data'), 400
    if not 'email' in data or data.get('email', '') == '':
        return infractuture_user_error_message('user_data'), 400
    if not 'password' in data or data.get('password', '') == '':
        return infractuture_user_error_message('user_data'), 400

    try:
        dto_input = CreateUserDTO(
            name     = data.get('name'),
            email    = data.get('email'),
            password = data.get('password')
        )
        create_user = CreateUserController(dto_input).execute()
        if 'error' in create_user:
            return create_user, 417
        return order_by_insert_JSON(create_user), 201
    except:
        return infractuture_user_error_message('create'), 503


ep_update_user = ep_user_private_routes('ep_update_user')


@api.route(ep_update_user['endpoint'], methods=ep_update_user['methods'])
@AuthService.auth_connection(request, fresh=False)
@process_request(request, get_rq=['data'], content_type='application/json')
def update_user(rq_info, current_user):

    data = rq_info['data']

    if not 'id' in data:
        return infractuture_user_error_message('user_data'), 400

    dto_input = UpdateUserDTO(
        id       = data.get('id'),
        name     = data.get('name'),
        email    = data.get('email'),
        password = data.get('password'),
    )
    update_user = UpdateUserController(dto_input).execute()
    try:
        if 'error' in update_user:
            return update_user, 417
        return order_by_insert_JSON(update_user)
    except:
        return infractuture_user_error_message('update'), 503


ep_delete_user = ep_user_private_routes('ep_delete_user')


@api.route(ep_delete_user['endpoint'], methods=ep_delete_user['methods'])
@AuthService.auth_connection(request, fresh=False)
@process_request(request, get_rq=['data'], content_type='application/json')
def delete_user(rq_info, current_user):
    data = rq_info['data']

    if not 'id' in data:
        return infractuture_user_error_message('user_data'), 400

    try:
        id_ = data.get('id')
        delete_user = DeleteUserController(id_).execute()
        if 'error' in delete_user:
            return delete_user, 417
        return delete_user
    except:
        return infractuture_user_error_message('delete'), 503
