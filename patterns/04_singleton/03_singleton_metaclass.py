class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    _instance = None

    def __init__(self) -> None:
        print("Loading a database from file")


if __name__ == "__main__":
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
