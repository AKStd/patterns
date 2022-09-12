from random import randint


class Generator:
    def generate(self, count: int) -> list:
        return [randint(1, 9) for x in range(count)]


class Splitter:
    def split(self, array):
        result = []

        row_count = len(array)
        col_count = len(array[0])

        for r in range(row_count):
            the_row = []
            for c in range(col_count):
                the_row.append(array[r][c])
            result.append(the_row)

        for c in range(col_count):
            the_col = []
            for r in range(row_count):
                the_col.append(array[r][c])
            result.append(the_col)

        diag1 = []
        diag2 = []

        for c in range(col_count):
            for r in range(row_count):
                if c == r:
                    diag1.append(array[r][c])
                r2 = row_count - r - 1
                if c == r2:
                    diag2.append(array[r][c])

        result.append(diag1)
        result.append(diag2)

        return result


class Verifier:
    def verify(self, arrays):
        first = sum(arrays[0])

        for i in range(1, len(arrays)):
            if sum(arrays[i]) != first:
                return False

        return True


class MagicSquareGenerator:
    def __init__(self) -> None:
        self.generator = Generator()
        self.splitter = Splitter()

    def generate(self, size: int) -> list:
        return self._split([self._generate(size) for _ in range(size)])

    def _generate(self, size: int) -> list:
        return self.generator.generate(size)

    def _split(self, arrays: list) -> list:
        return self.splitter.split(arrays)


# код ниже руками не трогать
# size = sys.stdin.read()
size = 2
gen = MagicSquareGenerator()
square = gen.generate(int(size))

v = Verifier()
print(v.verify(square))
