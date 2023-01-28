API_ADM = '/gestion'
USER = '/user'
API_ADM_USER = API_ADM + USER


def ep_user_private_routes(route: str) -> str:
    api_user_private_routes = {
        'ep_get_users'        : {
            'endpoint'  : API_ADM_USER,
            'methods'   : ['POST']
        },
        'ep_get_user_profile'      : {
            'endpoint'  : API_ADM_USER + '/profile',
            'methods'   : ['GET']
        },
        'ep_create_user'      : {
            'endpoint'  : API_ADM_USER + '/create',
            'methods'   : ['PUT']
        },
        'ep_update_user'      : {
            'endpoint'  : API_ADM_USER + '/update',
            'methods'   : ['PUT']
        },
        'ep_delete_user'      : {
            'endpoint'  : API_ADM_USER + '/delete',
            'methods'   : ['DELETE']
        }, 
        'ep_get_user_by_id'   : {
            'endpoint'  : API_ADM_USER + '/id',
            'methods'   : ['POST']
        },
        'ep_get_user_by_email': {
            'endpoint'  : API_ADM_USER + '/email',
            'methods'   : ['POST']
        }
    }
    
    try:
        return api_user_private_routes[route]
    except:
        raise ValueError('Invanlid route ' + route)