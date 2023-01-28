from app.api.user.infractucture.schemas.user_search__schema import user_search_schema
from app import ctx_db
from .queries__mongodb import Queries
from .command__mongodb import Command

class UserDB:
    
    def __init__(self):
        ''' User DB'''

    def count_user_found(search: str, field: str) -> int:
        query = {field:{ '$regex': search, '$options' :'i' }} if (search != "" and field != "") else {}
        return Queries(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').get_count(query)

    def get_users(page: int, per_page: int, order_by: str, sort_field: str):
        query={}
        pagination={ 'page': page, 'per_page': per_page, 'order_by': order_by, 'sort_field':sort_field}
        return Queries(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').find_with_pagination(query,pagination)

    def get_user_by_id(id: str) -> dict:
        query = {'_id' : id}
        return Queries(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').find_one(query)

    def get_user_by_email(email: str) -> dict:
        query = {'email' : email}
        return Queries(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').find_one(query)

    def get_user_idx(start: int, field_name: str) -> bool:
        result = Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='counters').get_next_idx(start,field_name)
        return result["sequence_value"]

    def create_index_field(field_name: str, index_name: str) -> bool:
        return Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').create_index(field_name,index_name)

    def create_user(user: dict) -> bool:
        result = Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').insert_one(user)
        if result.acknowledged:
            return True
        return False

    def update_user(id_: str, update_data:dict) -> bool:
        filter_id  = {'_id': id_}
        new_values = { '$set': update_data }
        result = Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').update_one(filter_id,new_values)
        if result and result.modified_count == 1:
            return True
        return False

    def delete_user(id_: str) -> bool:
        query = {'_id' : id_}
        result = Command(ctx_db = ctx_db, db_name = 'app_alexpddd', cl_name='users').delete_one(query)
        if result and result.deleted_count == 1:
            return True
        return False
