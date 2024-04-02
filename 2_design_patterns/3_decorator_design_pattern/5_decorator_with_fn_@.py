import logging
from math import sqrt
from time import perf_counter
from typing import Callable, Any
import functools


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for element in range(2, int(sqrt(number) + 1)):
        if number % element == 0:
            return False

    return True


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time}")
        return value
    return wrapper


def with_logging(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        logging.info(f"Calling {func.__name__}")
        value = func(*args, **kwargs)
        logging.info(f"Finished Calling {func.__name__}")
        return value
    return wrapper


@with_logging
@benchmark
def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count = count + 1

    return count


logging.basicConfig(level=logging.INFO)
count = count_prime_numbers(100000)
logging.info(f"Total number of prime number are {count}")
