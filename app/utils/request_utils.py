from functools import wraps
from flask import request, abort
from marshmallow import ValidationError


def validate_request(schema_cls):
    """This is a decorator for Marshmallow sschema requests validation

    Args:
        schema_cls (class object: Marshmallow schema)

    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            schema = schema_cls()
            try:
                data = schema.load(dict(request.values))
                return func(self, data)
            except ValidationError as e:
                abort(400, e.messages)
        return wrapper
    return decorator
