from app.services.factory__error import FactoryErrors

def auth_error_message(message: str) -> str:
    messages = {
        'default'               : 'Auth failed.',
        'user_data'             : 'Error data.',
        'unknown'               : 'Unknown error.'
    }
    return messages[message] if message in messages else messages['default']

def auth_app_error_message(action_message:str)->dict:
    message = auth_error_message(action_message)
    return FactoryErrors.error_message(message)