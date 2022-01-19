from functools import wraps
from flask import request

def verify_keys():
    trusted_keys = ["title", "author", "tags", "content"]
    def test_key(func):
        @wraps(func)
        def wraped_function():
            try:
                data = request.get_json()
                for key in trusted_keys:
                    data[key]
                return func()
            except KeyError:
                return {
                    "error": "chave(s) incorreta(s)",
                    "expected": trusted_keys,
                    "received": list(data.keys())
                   }, 400
        return wraped_function
    return test_key


