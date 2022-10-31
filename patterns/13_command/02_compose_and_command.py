import typing
import unittest
from abc import ABC
from enum import Enum


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance: int = 0) -> None:
        self.balance = balance

    def __str__(self) -> str:
        return f"Balance {self.balance}"

    def deposit(self, amount: int) -> None:
        self.balance += amount
        print(f"Deposit {amount}, {self}")

    def withdraw(self, amount) -> bool:
        result = False
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            result = True
            print(f"Withdraw {amount}, {self}")
        return result


class Command(ABC):
    def __init__(self):
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account: BankAccount, action: Action, amount: int) -> None:
        super().__init__()
        self.action = action
        self.account = account
        self.amount = amount

    def invoke(self) -> None:
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self) -> None:
        if not self.success:
            return

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)

        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items: typing.List[Command] = ""):
        super(CompositeBankAccountCommand, self).__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        [cmd.invoke() for cmd in self]

    def undo(self):
        [cmd.undo() for cmd in reversed(self)]


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acc: BankAccount, to_acc: BankAccount, amount: int):
        super().__init__(
            [
                BankAccountCommand(
                    from_acc, BankAccountCommand.Action.WITHDRAW, amount
                ),
                BankAccountCommand(to_acc, BankAccountCommand.Action.DEPOSIT, amount),
            ]
        )

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 100)
        deposit2 = BankAccountCommand(ba, BankAccountCommand.Action.DEPOSIT, 50)
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(ba)

        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        amount = 100
        wc = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)
        transfer = CompositeBankAccountCommand(
            [
                wc,
                dc,
            ]
        )
        transfer.invoke()

        transfer.undo()

    def test_transfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()
        amount = 10
        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print(f"ba1: {ba1}, ba2: {ba2}")
        transfer.undo()
        print(f"ba1: {ba1}, ba2: {ba2}")
        print(transfer.success)


if __name__ == "__main__":
    unittest.main()
