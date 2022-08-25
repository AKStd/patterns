class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    _instance = None

    def __init__(self, filename: str) -> None:
        self.populations = {}
        with open(filename) as file:
            for line in file:
                self.populations[line[0]] = line[1]
