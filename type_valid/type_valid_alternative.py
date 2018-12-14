# import inspect
# from functools import wraps
#
#
# def type_check(func):
#     """Decorator for type-checking parameters of the function"""
#
#     @wraps(func)
#     def check_types(*args, **kwargs):
#         args_names = inspect.getfullargspec(func).args
#         annotations = inspect.getfullargspec(func).annotations
#         # getting all types from annotations
#         types = []
#         for arg_name in args_names:
#             if arg_name in annotations:
#                 types.append(annotations[arg_name])
#             else:
#                 raise SyntaxError('all types must be specified')
#
#         # getting return type
#         return_type = None
#         if 'return' in annotations:
#             return_type = annotations['return']
#
#         # checking that args match their types or not exist
#         for argument, type in zip((args), types):
#             if not isinstance(argument, type) and argument is not None:
#                 raise TypeError("{} should be a {} instance".format(argument, type))
#
#         # checking that kwargs match their types or not exist
#         for keyword in kwargs:
#             argument = kwargs[keyword]
#             type = types[args_names.index(keyword)]
#             if not isinstance(argument, type) and argument is not None:
#                 raise TypeError("{} should be a {} instance".format(argument, type))
#
#         # checking that result match their type or not exist
#         result = func(*args, **kwargs)
#         if return_type is not None and not isinstance(result, return_type):
#             raise TypeError("{} should be a {} instance".format(result, return_type))
#
#         return result
#
#     return check_types