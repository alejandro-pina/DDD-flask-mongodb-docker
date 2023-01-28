from app.services.mongodb.errors.service__error import service_error_message
import pymongo

class Command:
    def __init__(self, ctx_db, db_name, cl_name):
        self.db = ctx_db.db[db_name][cl_name]

    def create_index(self, field_name, index_name):
        try:
            return self.db.create_index([(field_name, pymongo.ASCENDING)], unique=True, background=True, name=index_name)
        except pymongo.errors.DuplicateKeyError as e:
            return service_error_message('db_create_index')

    def create_index_expires(self, index_name, expire_after):
        try:
            return self.db.create_index(index_name, expireAfterSeconds=expire_after, unique=True)
        except:
            return service_error_message('db_create_index')

    def find_one_and_update(self, filter_field:str, query: dict):
        try:
            return self.db.find_one_and_update(filter_field,query, upsert=True, return_document=True)
        except:
            return service_error_message('db_find_one_and_update')

    def get_next_idx(self, start, field_name):
        try:
            return self.db.find_one_and_update({"_id": field_name}, {"$inc": {"sequence_value": start}}, return_document=pymongo.ReturnDocument.AFTER, upsert=True)
        except:
            return service_error_message('db_get_idx')
    
    def insert_one(self, query: dict):
        try:
            return self.db.insert_one(query)
        except:
            return service_error_message('db_insert_one')

    def insert_many(self, data: dict):
        try:
            return self.db.insert_many(data)
        except:
            return service_error_message('db_insert_many')

    def update_one(self, filter_field: dict, new_values: dict):
        try:
            return self.db.update_one(filter_field,new_values)
        except:
            return service_error_message('db_update_one')
    
    def update_many(self, filter_field: dict, new_values: dict):
        try:
            return self.db.update_many(filter_field,new_values)
        except:
            return service_error_message('db_update_many')

    def delete_one(self, query: dict):
        try:
            return self.db.delete_one(query)
        except:
            return service_error_message('db_delete_one')

    def delete_many(self, query: dict):
        try:
            return self.db.delete_many(query)
        except:
            return service_error_message('db_delete_many')