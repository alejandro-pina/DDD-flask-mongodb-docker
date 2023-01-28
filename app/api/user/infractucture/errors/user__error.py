from app.services.factory__error import FactoryErrors

def req_messages(message:str)->str:
    messages = {
        'default'    : 'Service connection error.',
        'create'     : 'Could not create user.',
        'update'     : 'Could not update user.',
        'delete'     : 'Could not delete user.',
        'id'         : 'User could not be found by id.',
        'email'      : 'User could not be found by email.',
        'users'      : 'Could not get users.',
        'user_data'  : 'Error user data.',
        'user_model' : 'Wrong data to create user model.'
    }
    return messages[message] if message in messages else messages['default']

def infractuture_user_error_message(action_message:str)->dict:
    message = req_messages(action_message)
    return FactoryErrors.error_message(message)