from typing import get_type_hints
from inspect import getfullargspec
from functools import wraps


def type_valid(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):

        # translate *args into **kwargs
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))

        # get hints type from object
        hints = get_type_hints(decorator)

        # default return type
        return_type = None

        # iterate all type hints
        for attr_name, attr_type in hints.items():

            # output get type for later validation
            if attr_name == 'return':
                return_type = attr_type
                continue

            # validate input
            try:
                if not isinstance(kwargs[attr_name], attr_type):
                    raise TypeError(
                        'in method %r, Argument %r is not of type %s, received %s'
                        % (decorator.__name__, attr_name, attr_type,
                            type(kwargs[attr_name]))

                    )
            except KeyError:
                raise TypeError(
                    'in method %r, Argument %r is required'
                    % (decorator.__name__, attr_name)
                )

        # process object to get output
        output = decorator(**kwargs)

        # validate return type
        if return_type is not None and not isinstance(output, return_type):
            raise TypeError(
                'in method %r, output %r is not of type %s, received %s' %
                (decorator.__name__, output, return_type, type(output))
            )

        # return original output
        return output

    return wrapped_decorator
