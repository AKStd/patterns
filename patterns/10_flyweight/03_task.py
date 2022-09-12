class Sentence:
    def __init__(self, plain_text: str):
        self.plain_text: str = plain_text
        self.formatting: list = []

    class WordRange:
        def __init__(self, position: int, capitalize=False) -> None:
            self.position: int = position
            self.capitalize: bool = capitalize

        def covers(self, position: int) -> bool:
            return self.position == position

    def get_position(self, position: int) -> "WordRange":
        _position = self.WordRange(position)
        self.formatting.append(_position)
        return _position

    def __getitem__(self, index: int) -> "WordRange":
        return self.get_position(index)

    def __str__(self) -> str:
        result: list = []
        for i in range(len(self.plain_text.split())):
            c = self.plain_text.split()[i]
            for fr in self.formatting:
                if fr.covers(i) and fr.capitalize:
                    c = c.upper()
            result.append(c)

        return " ".join(result)


# код ниже руками не трогать
# sentence, index = sys.stdin.read().split(':')
sentence, index = 'alpha beta gamma', 1

s = Sentence(sentence)
s[int(index)].capitalize = True

print(str(s))
