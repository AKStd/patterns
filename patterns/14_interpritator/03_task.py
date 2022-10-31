import typing
from enum import Enum, auto


class Integer:
    def __init__(self, value) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value}"


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self) -> None:
        self.type = None
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"left: {self.left}, right: {self.right}, type:{self.type}"

    @property
    def value(self) -> int:
        if not self.right:
            return self.left

        elif self.type == self.Type.ADDITION:
            return self.left.value + self.right.value

        else:
            return self.left.value - self.right.value


class Parser:
    @staticmethod
    def parse(tokens: list) -> BinaryExpression:
        result = BinaryExpression()
        have_lhs = False
        i = 0
        while i < len(tokens):
            token = tokens[i]

            if token.type == Token.Type.INTEGER:
                integer = Integer(int(token.text))

                if not have_lhs:
                    result.left = integer
                    have_lhs = True
                else:
                    result.right = integer
                    temp = Integer(int(result.value))
                    result = BinaryExpression()
                    result.left = temp
                    have_lhs = True

            elif token.type == Token.Type.PLUS:
                result.type = BinaryExpression.Type.ADDITION

            elif token.type == Token.Type.MINUS:
                result.type = BinaryExpression.Type.SUBTRACTION

            i += 1
        return result


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()

    def __init__(self, _type: Type, text: str) -> None:
        self.type = _type
        self.text = text

    def __repr__(self) -> str:
        return f"token :`{self.text}`"

    def __str__(self) -> str:
        return f"`{self.text}`"


class Unexpected(Exception):
    ...


class Analyzer:
    PLUS = Token.Type.PLUS
    MINUS = Token.Type.MINUS

    def lexical_analysis(self, _input: str) -> typing.List["Token"]:
        result = []
        i = 0
        while i < len(_input):
            if _input[i] == "+":
                result.append(Token(self.PLUS, "+"))
            elif _input[i] == "-":
                result.append(Token(self.MINUS, "-"))
            else:
                digits = [_input[i]]
                for j in range(i + 1, len(_input)):
                    if _input[j].isdigit():
                        digits.append(_input[j])
                        i += 1
                    else:
                        break
                result.append(Token(Token.Type.INTEGER, "".join(digits)))
            i += 1
        return result


class ExpressionProcessor:
    allowed_symbols = ["-", "+"]

    def __init__(self):
        self.variables = {}
        self.parser = Parser()
        self.analyzer = Analyzer()

    def map_variables(self, expression: str) -> str:
        _exp = ""
        for char in expression.strip():
            if char in self.allowed_symbols:
                _exp += char
            elif char.isdigit():
                _exp += char
            else:
                if self.variables.get(char, None):
                    _exp += str(self.variables.get(char, None))
                else:
                    raise Unexpected
        return _exp

    def calculate(self, expression) -> int:
        try:
            __expression = self.map_variables(expression)
            tokens = self.analyzer.lexical_analysis(__expression)
            return getattr(self.parser.parse(tokens), "value")
        except Unexpected:
            return 0


# В тестах, х=5 всегда
# код ниже руками не трогать
ep = ExpressionProcessor()
ep.variables["x"] = 5

print(ep.calculate("1 "))
