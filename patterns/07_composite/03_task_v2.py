import sys
from abc import ABC
from collections.abc import Iterable


class Summable(Iterable, ABC):
    @property
    def sum(self):
        return sum(self)


class SingleValue(int, Summable):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, Summable):
    def __init__(self):
        super().__init__()

    def __radd__(self, other):
        result = other

        for x in self:
            result += x

        return result


# код ниже руками не трогать
a, b, c = sys.stdin.read().split()
single_value = SingleValue(int(a))
other_values = ManyValues()
other_values.append(int(b))
other_values.append(int(c))

all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)

print(all_values.sum)
