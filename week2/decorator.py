import json

def to_json(func):
    def decorated(*args,**kwargs):
        return