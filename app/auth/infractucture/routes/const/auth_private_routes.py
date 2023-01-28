def ep_auth_private_routes(route: str) -> str:

    api_auth_private_routes = {
        'epa_auth'    : {
            'endpoint': '/',
            'methods' : ['GET']
        },
        'epa_logout'  : {
            'endpoint': '/logout',
            'methods' : ['PUT']
        }
    }
    
    try:
        return api_auth_private_routes[route]
    except:
        raise ValueError('Invanlid route ' + route)
