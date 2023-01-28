from app.services.factory__error import FactoryErrors


def vo_messages(message: str) -> str:
    messages = {
        'default'   : 'Error user data.',
        'email'     : 'The email is wrong.',
        'field_date': 'The field date is wrong.',
        'idx'       : 'Error idx.',
        'name'      : 'The name is wrong.',
        'order_by'  : 'The order by is wrong.',
        'page'      : 'The page is wrong.',
        'password'  : 'The password is wrong.',
        'users'     : 'The data is wrong.',
        'short_str' : 'Wrong string.',
        'sort_by'   : 'The sort by is wrong.',
        'id'        : 'The id is wrong.',
        'create'    : 'Error create user.',
        'update'    : 'Error update user.',
        'login'     : 'Error user login.',
    }
    return messages[message] if message in messages else messages['default']


def domain_user_error_message(action_message: str) -> dict:
    message = vo_messages(action_message)
    return FactoryErrors.error_message(message)
