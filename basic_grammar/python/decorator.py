'''
EX1: Decorator to count the number of times a function is called.
'''
from functools import wraps
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of {func.__name__}")
        return func(*args, **kwargs)
    
    # Initialize the call count
    wrapper.calls = 0
    return wrapper

@count_calls
def say_hello(name):
    """Print a greeting to the user."""
    print(f"Hello, {name}!")
    
# Test if the "calls" attribute is respective to different functions 
@count_calls
def say_goodbye(name):
    """Print a farewell to the user."""
    print(f"Goodbye, {name}!")

say_hello("Alice")
say_hello("Bob")
say_goodbye("Alice")
say_goodbye("Bob")
say_hello("Charlie")
say_goodbye("Charlie")


'''
EX2: Decorator to log the time taken by a function to execute.
'''
def time_logger(level="DEBUG"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            import time
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"{level}: {func.__name__} took {elapsed_time:.4f} seconds, result: {result}")
            return result
        return wrapper
    return decorator

@time_logger(level="INFO")
def compute_sum(n):
    """Compute the sum of the first n natural numbers."""
    return sum(range(n + 1))

compute_sum(19911007)