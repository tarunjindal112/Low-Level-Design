import logging
from math import sqrt
from time import perf_counter
from typing import Callable, Any


def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for element in range(2, int(sqrt(number) + 1)):
        if number % element == 0:
            return False

    return True


def count_prime_numbers(upper_bound: int) -> int:
    count = 0
    for number in range(upper_bound):
        if is_prime(number):
            count = count + 1

    return count


def benchmark(func: Callable[..., Any]) -> Callable[..., Any]:
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(f"Execution of {func.__name__} took {run_time}")
        return value
    return wrapper


logging.basicConfig(level=logging.INFO)
wrapper = benchmark(count_prime_numbers)
count = wrapper(100000)
logging.info(f"Total number of prime number are {count}")
