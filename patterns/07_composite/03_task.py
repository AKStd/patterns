import sys
from abc import ABC
from collections.abc import Iterable


class SingleValue:
    def __init__(self, value):
        self.value = value


class ManyValues(list):
    @property
    def sum(self) -> int:
        __sum = 0
        for e in self:
            if isinstance(e, SingleValue):
                __sum += e.value
            elif isinstance(e, ManyValues):
                __sum += e.sum
            elif isinstance(e, int):
                __sum += e
            else:
                raise TypeError(f"Incorrect type od element {e}: {type(e)}")
        return __sum


# код ниже руками не трогать
a, b, c = ["11", "22", "33"]
single_value = SingleValue(int(a))
other_values = ManyValues()
other_values.append(int(b))
other_values.append(int(c))

all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)

print(all_values.sum)
