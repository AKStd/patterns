from typing import Callable


def singleton(class_: Callable) -> Callable:
    instances = {}

    def get_instance(*args, **kwargs) -> Callable:
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    _instance = None

    def __init__(self) -> None:
        print('Loading a database from file')


if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
