import sys
import typing


# ваше решение
class CodeBuilder:
    indent_size = 2

    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.fields = []

    def add_field(self, attr: str, value: typing.Any) -> "CodeBuilder":
        self.fields.append((attr, value))
        return self

    def __str(self) -> str:
        lines = [
            f"class {self.root_name}:",
        ]
        func_indent = " " * self.indent_size
        if self.fields:
            lines.append(f"{func_indent}def __init__(self):")
            for attr, value in self.fields:
                attr_indent = " " * self.indent_size + func_indent
                lines.append(f"{attr_indent}self.{attr} = {value}")
        else:
            lines.append(f"{func_indent}pass")

        return "\n".join(lines)

    def __str__(self) -> str:
        return self.__str()


cb = CodeBuilder("Foo")
print(cb)

cb = CodeBuilder("Person").add_field("name", '""').add_field("age", "0")
print(cb)

# # код ниже руками не трогать
# def preprocess(s=''):
#     return s.strip().replace('\r\n', '\n')
#
#
# input_args = sys.stdin.read().split(',')
# cb = CodeBuilder(input_args[0])
# if (len(input_args) > 1):
#     cb.add_field(input_args[1].split(':')[0], input_args[1].split(':')[1])
#     cb.add_field(input_args[2].split(':')[0], input_args[2].split(':')[1])
#
# print(preprocess((str(cb))))
