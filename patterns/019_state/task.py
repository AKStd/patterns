import sys


class CombinationLock:
    def __init__(self, combination: list) -> None:
        self.status = 'LOCKED'
        self.combination = combination
        self.buffer = list()

    def reset(self) -> None:
        self.status = 'LOCKED'

    @staticmethod
    def list_to_str(_list: list) -> str:
        return "".join((str(i) for i in _list))

    def __set_status(self) -> None:
        if self.list_to_str(self.buffer) == self.list_to_str(self.combination):
            self.status = "OPEN"
        else:
            self.status = "ERROR"

    def enter_digit(self, digit: int) -> None:
        self.buffer.append(digit)
        if len(self.combination) == len(self.buffer):
            self.__set_status()
        else:
            self.status = self.list_to_str(self.buffer)


def test(dataset):
    right_str, entered_str = dataset.split(';')

    right = [int(x) for x in right_str.split()]
    entered = [int(x) for x in entered_str.split()]

    cl = CombinationLock(right)
    result = f'{cl.status} '

    for x in entered:
        cl.enter_digit(x)
        result += f'{cl.status} '

    return result


result = test(sys.stdin.read())
print(result)
