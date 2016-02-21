__author__ = 'magus0219'


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            ret = None
            run_times = 0
            succeed = False
            while run_times <= times and not succeed:
                try:
                    ret = func(*args, **kwargs)
                    succeed = True
                except Exception as ex:
                    if run_times < times:
                        run_times += 1
                    else:
                        raise ex

            return ret

        return wrapper

    return decorator
