from app.services.factory__error import FactoryErrors


def user_messages(message: str) -> str:
    messages = {
        'default'                        : 'The action on the user could not be performed.',
        'user_exist'                     : 'User not exist',
        'users_imported'                 : 'Failed to import users.',
        'users_already_imported'         : 'The users you are trying to import have already been imported.',
        'failed_service_user_import'     : 'TThe service that import the user has failed.',
        'user_create'                    : 'The user could not be created.',
        'failed_service_user_user_create': 'The service that creates the user has failed.',
        'user_email'                     : 'Email exist. The user could not be created.',
        'email_exist'                    : 'The given email is in use.',
        'user_read'                      : 'The user could not be readed.',
        'user_update'                    : 'The user could not be updated.',
        'failed_service_user_update'     : 'The service that updates the user has failed.',
        'user_delete'                    : 'The user could not be deleted.',
        'failed_service_user_delete'     : 'The service that deletes the user has failed.',
        'user_date'                      : 'Error date range.',
        'failed_service_search_user'     : 'The service that search the user has failed.',
        'failed_service_search_by_user'  : 'The user search by id service has failed.',
        'user_not_found'                 : 'User not found.',
        'failed_service_get_user'        : 'The user search service has failed.',
        'user_register'                  : 'User in use.',
        'user_data'                      : 'Error data.',
        'user_token'                     : 'Error token.',
        'tkr'                            : 'Access denied.',
        'user_device'                    : 'You are trying to sign in from a new device or a different connection to access your credentials.',
        'user_ban'                       : 'Your account has been suspended.',
        'unknown'                        : 'unknown error.'
    }
    return messages[message] if message in messages else messages['default']


def app_error_message(action_message: str) -> dict:
    message = user_messages(action_message)
    return FactoryErrors.error_message(message)
