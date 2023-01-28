import json 

def order_by_insert_JSON(resp):
    if not isinstance(resp,dict): return resp
    return json.dumps(resp)