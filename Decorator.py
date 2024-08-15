def my_decorator(*args, my_param1=None, my_param2=None):
    # my_param1 и my_param2 - optional parameters
    def _my_decorator(f):
        def wrap(*args, **kwargs):
            print('my_param1', my_param1)
            print('my_param2', my_param2)

            # Something BEFORE function
            result = f(*args, **kwargs)
            # Something AFTER function
            return result
        return wrap
    if len(args) == 1 and callable(args[0]):
        return _my_decorator(args[0])    # decorate without parameters
    else:
        return _my_decorator             # decorate with parameters