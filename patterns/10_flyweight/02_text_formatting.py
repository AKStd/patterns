class FormattedText:
    def __init__(self, plain_text: str) -> None:
        self.plain_text: str = plain_text
        self.caps: list = [False] * len(plain_text)

    def capitalize(self, start: int, end: int) -> None:
        for i in range(start, end):
            self.caps[i] = True

    def __str__(self) -> str:
        result: list = []
        for i in range(len(self.plain_text)):
            c: str = self.plain_text[i]
            result.append(
                c.upper() if self.caps[i] else c
            )
        return "".join(result)


class BetterFormattedText:
    def __init__(self, plain_text: str):
        self.plain_text: str = plain_text
        self.formatting: list = []

    class TextRange:
        def __init__(self, start: int, end: int, capitalize=False) -> None:
            self.start: int = start
            self.end: int = end
            self.capitalize: bool = capitalize

        def covers(self, position: int) -> bool:
            return self.start <= position <= self.end

    def get_range(self, start: int, end: int) -> "TextRange":
        _range = self.TextRange(start, end)
        self.formatting.append(_range)
        return _range


    def __str__(self) -> str:
        result: list = []
        for i in range(len(self.plain_text)):
            c = self.plain_text[i]
            for fr in self.formatting:
                if fr.covers(i) and fr.capitalize:
                    c = c.upper()
            result.append(c)

        return "".join(result)


if __name__ == "__main__":
    text = "This is a brave new world"
    ft = FormattedText(text)
    ft.capitalize(10, 15)
    print(ft)

    bft = BetterFormattedText(text)
    bft.get_range(16, 19).capitalize = True
    print(bft)
