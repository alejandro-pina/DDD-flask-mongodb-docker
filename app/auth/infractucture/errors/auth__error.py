from app.services.factory__error import FactoryErrors

def error_messages(message: str) -> str:
    messages = {
        'default'     : 'Auth Failed.',
        'auth_data'   : 'The data entered is not correct.',
        'login'       : 'Failed login.',
        'logout'      : 'Failed logout.',
        'unknown'     : 'Unknown.'
    }
    return messages[message] if message in messages else messages['default']

def auth_infractuture_error_message(action_message: str) -> dict:
    message = error_messages(action_message)
    return FactoryErrors.error_message(message)