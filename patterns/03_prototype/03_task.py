import copy
import sys


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: "Point" = Point(), end: "Point" = Point()) -> None:
        self.start = start
        self.end = end

    def deep_copy(self) -> "Line":
        return copy.deepcopy(self)


# код ниже руками не трогать:
coords = sys.stdin.read().split()
line1 = Line(
    Point(int(coords[0]), int(coords[1])), Point(int(coords[2]), int(coords[3]))
)
line2 = line1.deep_copy()
line1.start.x = line1.end.x = line1.start.y = line1.end.y = 0

print(f"{line2.start.x} {line2.start.y} {line2.end.x} {line2.end.y}")
