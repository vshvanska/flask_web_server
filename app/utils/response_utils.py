from functools import wraps


def serialize_response(schema_cls):
    """This is a decorator for Marshmallow sschema response serialization

    Args:
        schema_cls (class object: Marshmallow schema)

    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            schema = schema_cls()
            item, status_code = func(self, *args, **kwargs)
            response_data = (schema.dump(item))
            return response_data, status_code
        return wrapper
    return decorator
