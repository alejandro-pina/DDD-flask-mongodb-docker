class FactoryErrors:
    def defaultMessage():
        return {"error":"💣"}

    def error_message(message,back_to=None):
        resp = {
            'error' : message
        }
        if back_to: resp["back_to"] = back_to
        return resp
