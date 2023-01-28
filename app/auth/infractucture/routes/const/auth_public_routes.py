def ep_auth_public_routes(route: str) -> str:

    api_auth_public_routes = {
        'epa_login'   : {
            'endpoint': '/login',
            'methods' : ['POST']
        }
    }

    try:
        return api_auth_public_routes[route]
    except:
        raise ValueError('Invanlid route ' + route)
