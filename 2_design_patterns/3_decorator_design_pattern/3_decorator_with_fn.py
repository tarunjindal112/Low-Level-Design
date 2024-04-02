import logging
from math import sqrt
from time import perf_counter


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


def benchmark(upper_bound: int) -> int:
    start_time = perf_counter()
    value = count_prime_numbers(upper_bound)
    end_time = perf_counter()
    run_time = end_time - start_time
    logging.info(f"Execution of count_prime_numbers took {run_time}")
    return value


logging.basicConfig(level=logging.INFO)
count = benchmark(100000)
logging.info(f"Total number of prime number are {count}")
