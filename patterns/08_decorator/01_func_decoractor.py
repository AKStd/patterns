import time


def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"func {func.__name__} took {int((end - start) * 1000)}")
        return result

    return wrapper


@time_it
def some_op():
    print("Starting op")
    time.sleep(1)
    print("Done")
    return 123


if __name__ == "__main__":
    some_op()
    # time_it(some_op)()
