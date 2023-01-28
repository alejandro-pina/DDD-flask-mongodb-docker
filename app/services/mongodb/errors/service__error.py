from app.services.factory__error import FactoryErrors

def req_messages(message: str) -> str:
    messages = {
        'default'               : 'Error service.',
        'db_connection'         : 'Error connection to database.',
        'db_type_query'         : 'Error query type unknown.',
        'db_query'              : 'Error query in database.',
        'db_command'            : 'Error command in database.',
        'db_find_one_and_update': 'Error find and update in database.',
        'db_insert_one'         : 'Error insert in database.',
        'db_insert_many'        : 'Error insert many in database.',
        'db_update_one'         : 'Error update in database.',
        'db_update_many'        : 'Error update many in database.',
        'db_delete_one'         : 'Error delete in database.',
        'db_delete_many'        : 'Error delete many in database.',
        'db_wrong_query'        : 'Error wrong query send.',
        'db_count'              : 'Error counting documents.',
        'db_paging'             : 'Error paging documents.',
        'db_find_last'          : 'Error finding last document.',
        'db_find_first'         : 'Error finding first document.',
        'db_get_idx'            : 'Error get idx in collection.',
        'db_find_one'           : 'Error finding document.',
        'db_find'               : 'Error finding documents.'
    }
    return messages[message] if message in messages else messages['default']

def service_error_message(action_message: str) -> dict:
    message = req_messages(action_message)
    return FactoryErrors.error_message(message)