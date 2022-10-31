import random
import string


class User:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return f"User: {self.name}"


class User2:
    strings: list = []

    def __init__(self, full_name: str) -> None:
        def get_or_add(s: str) -> int:
            _index: int = len(self.strings)
            if s not in self.strings:
                self.strings.append(s)
            else:
                _index = self.strings.index(s)
            return _index

        self.names: list = [get_or_add(x) for x in full_name.split(" ")]

    def __str__(self) -> str:
        return " ".join([self.strings[x] for x in self.names])


def random_string() -> str:
    chars: str = string.ascii_lowercase
    return "".join([random.choice(chars) for _ in range(8)])


if __name__ == "__main__":
    users = []
    first_names = [random_string() for _ in range(100)]
    last_names = [random_string() for _ in range(100)]

    for first in first_names:
        for last in last_names:
            users.append(User2(f"{first} {last}"))

    print(users[0])
