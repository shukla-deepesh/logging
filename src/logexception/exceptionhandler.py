import functools

class CustomDivideByZero(ZeroDivisionError):
    def __init__(self):
        print("Don't divide by zero stupid !")

class CustomTypeError(TypeError):
    def __init__(self):
        print( "Custom Type mismatch !")


def exception(logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(func):

        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except CustomDivideByZero:
                # log the exception
                err = "Type Error   "
                err += func.__name__
                logger.exception(err)
            except CustomTypeError:
                # log the exception
                err = "Type Mismatch   "
                err += func.__name__
                logger.exception(err)
            except TypeError:
                err = "Type Error   "
                err += func.__name__
                logger.exception(err)
            except:
                # log the exception
                err = "There was an exception in  "
                err += func.__name__
                logger.exception(err)

        return wrapper

    return decorator