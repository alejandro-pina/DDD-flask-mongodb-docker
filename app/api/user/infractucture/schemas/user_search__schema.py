def user_search_schema(data_object: dict) -> dict:
    users = data_object.get('users') if data_object.get('users') and isinstance(data_object.get('users'),list) else []
    total = data_object.get('total') if data_object.get('total') and isinstance(data_object.get('total'),int) else 0

    return {
        "users" : users,
        "total": total,
    }