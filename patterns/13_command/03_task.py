import sys

from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action, amount: int):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int) -> bool:
        self.balance += amount
        return True

    def withdraw(self, amount: int) -> bool:
        result = False
        if self.balance - amount >= 0:
            self.balance -= amount
            result = True
        return result

    def process(self, command: "Command") -> bool:
        if command.action == Command.Action.DEPOSIT:
            command.success = self.deposit(command.amount)
        elif command.action == Command.Action.WITHDRAW:
            command.success = self.withdraw(command.amount)
        return command.success

    # код ниже руками не трогать


input_args = ["100", "-50", "-150"]
a = Account()

result = ""
for x in input_args:
    amount = int(x)
    cmd = None
    if amount > 0:
        cmd = Command(Command.Action.DEPOSIT, amount)
    elif amount < 0:
        cmd = Command(Command.Action.WITHDRAW, amount * (-1))

    a.process(cmd)

    result += f"{a.balance} {cmd.success} "

print(result)
