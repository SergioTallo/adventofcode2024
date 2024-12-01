import functools
import time

def measure_time(func):
    """
    Measure the execution time of a function
    :param func: Function to measure
    :return: wrapper function
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        Wrapper function
        :param args: arguments
        :param kwargs: keyword arguments
        :return: result of the function
        """
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for '{func.__name__}': {execution_time} seconds")
        return result

    return wrapper