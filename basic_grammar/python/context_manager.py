'''
Context manager to suppress specific exceptions
'''
from contextlib import contextmanager

@contextmanager
def suppress_exception(exception_type):
    try:
        yield
    except Exception as e:
        if(isinstance(e, exception_type)):
            print(f"Exception {exception_type.__name__} suppressed")
        else:
            print(f"Exception {e.__class__.__name__} raised")
            raise

with suppress_exception(ValueError):
    print("Try to make a ValueError")
    x = int("not a number")  # This will raise ValueError
    print("This will not be printed if ValueError is raised above")

with suppress_exception(ValueError):
    print("Try to make a TypeError")
    x = 1 + "string"  # This will raise TypeError