from time import perf_counter, sleep
from random import uniform


def function_execution_time(func):
    def wrapper():
        time_start = perf_counter()
        func()
        time_end = perf_counter()
        print(f"Function execution time: {time_end-time_start} seconds")
    return wrapper


@function_execution_time
def func():
    sleep(uniform(0, 3))


if __name__ == '__main__':
    func()
