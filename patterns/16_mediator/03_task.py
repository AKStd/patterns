import sys


class Mediator(list):
    ...


class Participant:
    def __init__(self, mediator: "Mediator") -> None:
        self.value: int = 0
        self.mediator = mediator
        self.mediator.append(self)

    def say(self, value: int) -> None:
        for participant in self.mediator:
            if participant != self:
                participant.increase(value)

    def increase(self, value: int):
        self.value += value


# код ниже руками не трогать
x, y = sys.stdin.read().split()

m = Mediator()
p1 = Participant(m)
p2 = Participant(m)

result = f"{p1.value} {p2.value} "

p1.say(int(x))

result += f"{p1.value} {p2.value} "

p2.say(int(y))

result += f"{p1.value} {p2.value}"

print(result)
