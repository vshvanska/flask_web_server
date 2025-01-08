from functools import wraps


def validate_schema(schema_cls):
    """This is a decorator for Marshmallow sschema requests validation

    Args:
        schema_cls (class object: Marshmallow schema)

    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            schema = schema_cls()
            return func()
        return wrapper
    return decorator
