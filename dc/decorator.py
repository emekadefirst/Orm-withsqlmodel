# import functools

# def log_function_call(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} returned {result}")
#         return result
#     return wrapper

# @log_function_call
# def add(a, b):
#     return a + b


# add(2, 3)

import time
import functools

def timing_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} took {end_time - start_time:.4f} seconds to execute")
        return result
    return wrapper

@timing_decorator
def compute_squares(n):
    return [i * i for i in range(n)]

# Usage
compute_squares(10000)
