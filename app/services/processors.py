from functools import wraps
import json

class Processor:
    def __init__(self, mimetype=None):
        self.mimetype = mimetype
        self.pattern = None

    def process(self, data):
        raise NotImplementedError("process method must be implemented.")

class JsonProcessor(Processor):
    def __init__(self):
        super().__init__("application/json")

    def process(self, data):
        try:
            data = json.loads(data)
            if not bool(data):
                raise ValueError("json void")
        except json.decoder.JSONDecodeError:
            raise ValueError("Invalid json format")
        return data

processors = {
    "application/json": JsonProcessor(),
    # More processor
}

def process_request(request, get_rq = [], content_type = ''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request_data = ''
            
            if content_type:
                request_content_type = request.content_type
                if request_content_type != content_type or request_content_type not in processors:
                    return {
                        "error": "Unsupported data."
                    }, 400
                try:
                    request_data = processors[request_content_type].process(request.data)
                except ValueError as e:
                    return {
                        "error": f" Wrong data."
                    }, 400
            rq_info = {}
            rq_info_values = {
                'data'       : request_data,
                'path'       : request.path
                # More fields
            }
            for field in get_rq:
                if field in rq_info_values:
                    rq_info[field] = rq_info_values[field]
                else:
                    return {
                        "error": "INFO data."
                    }, 400
            return func(rq_info, *args, **kwargs)
        return wrapper
    return decorator