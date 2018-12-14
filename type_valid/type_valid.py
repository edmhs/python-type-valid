from typing import get_type_hints
from inspect import getfullargspec
from functools import wraps

# inspiration from https://aboutsimon.com/blog/2018/04/04/Python3-Type-Checking-And-Data-Validation-With-Type-Hints.html


def validate_input(obj, **kwargs):
    hints = get_type_hints(obj)

    # iterate all type hints
    for attr_name, attr_type in hints.items():
        if attr_name == 'return':
            continue

        if not isinstance(kwargs[attr_name], attr_type):
            raise TypeError(
                'in method %r, Argument %r is not of type %s, received %s' % (obj.__name__, attr_name, attr_type, type(kwargs[attr_name]))
            )


def type_valid(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        # translate *args into **kwargs
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        validate_input(decorator, **kwargs)
        return decorator(**kwargs)

    return wrapped_decorator
