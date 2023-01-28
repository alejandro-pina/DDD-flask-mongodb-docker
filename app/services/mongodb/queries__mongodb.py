from app.services.mongodb.errors.service__error import service_error_message

class Queries:
    def __init__(self, ctx_db, db_name, cl_name):
        self.db = ctx_db.db[db_name][cl_name]

    def find(self, query:dict)->list:
        try:
            return list(self.db.find(query))
        except:
            return service_error_message('db_find')

    def find_with_pagination(self, query: dict, pagination: dict )->list:
        page       = pagination.get('page', None)
        order_by   = pagination.get('order_by', None)
        sort_field = pagination.get('sort_field', None)
        per_page   = pagination.get('per_page', None)

        data = {}
        if page and per_page and order_by and sort_field:
            try:
                sort, skip, limit = self.get_pagination(page, per_page, order_by, sort_field)
                data = list(self.db.find(query).collation({'locale':'en'}).sort(sort).skip(skip).limit(limit))
            except:
                return service_error_message('db_paging')

        elif page and per_page:
            try:
                data = list(self.db.find(query).collation({'locale':'en'}).sort(sort).skip(per_page*(page-1)).limit(per_page))
            except:
                return service_error_message('db_paging')
        else:
            return service_error_message('db_paging')
        return data

    def find_one(self, query:dict)->list:
        try:
            return self.db.find_one(query)
        except:
            return service_error_message('db_find_one')

    def get_pagination(self, page: int, per_page: int, order_by: str, sort_field: str) -> list:
        order_by = -1 if (order_by == "desc") else 1
        sort     = [(sort_field, order_by)]
        pagesize = limit =  per_page
        limit    = per_page
        skip     = pagesize*(page-1)
        return [sort,skip,limit]

    def get_count(self, query: dict) -> int:
        try:
            total = self.db.count_documents(query)
            if total and total > 0: 
                return total
            return 0
        except:
            return service_error_message('db_count')

    def last_document(self, query: dict):
        try:
            return self.db.find({}).sort(query).limit(1)[0]
        except:
            return service_error_message('db_find_last')

    def first_document(self, query: dict):
        try:
            return self.db.find({}).sort(query).limit(1)[0]
        except:
            return service_error_message('db_find_first')


    

