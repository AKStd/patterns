from enum import Enum, auto


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, _type: Type, text: str):
        self.type = _type
        self.text = text

    def __repr__(self):
        return f"token - `{self.text}`"

    def __str__(self):
        return f"`{self.text}`"


def lex(_input: str):
    result = []
    i = 0
    while i < len(_input):
        if _input[i] == "+":
            result.append(Token(Token.Type.PLUS, "+"))
        elif _input[i] == "-":
            result.append(Token(Token.Type.MINUS, "-"))
        elif _input[i] == "(":
            result.append(Token(Token.Type.LPAREN, "("))
        elif _input[i] == ")":
            result.append(Token(Token.Type.RPAREN, ")"))
        else:
            digits = [_input[i]]
            for j in range(i + 1, len(_input)):
                if _input[j].isdigit():
                    digits.append(_input[j])
                    i += 1
                else:
                    result.append(Token(Token.Type.INTEGER, "".join(digits)))
                    break
        i += 1
    return result


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryExpression:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type = None
        self.left = None
        self.right = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        else:
            return self.left.value - self.right.value


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

        elif token.type == Token.Type.PLUS:
            result.type = BinaryExpression.Type.ADDITION

        elif token.type == Token.Type.MINUS:
            result.type = BinaryExpression.Type.SUBTRACTION

        elif token.type == Token.Type.LPAREN:
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            subexpression = tokens[i + 1 : j]

            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j
        i += 1
    return result


def calc(_input: str):
    tokens = lex(_input)
    print(" ".join(map(str, tokens)))
    parsed = parse(tokens)
    print(f"{_input} = {parsed.value}")


if __name__ == "__main__":
    calc("(13+4)-(12+1)")
