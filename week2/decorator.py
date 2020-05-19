from json import dumps
from functools import wraps

def to_json(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        return dumps(func(*args, **kwargs))
    return decorated()