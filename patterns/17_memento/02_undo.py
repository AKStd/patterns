import typing


class Memento:
    def __init__(self, balance: int) -> None:
        self.balance = balance


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance
        self.changes: typing.List["Memento"] = [
            Memento(self.balance),
        ]
        self.current: int = 0

    def deposit(self, amount: int) -> "Memento":
        self.balance += amount
        memento = Memento(self.balance)
        self.changes.append(memento)
        self.current += 1
        return memento

    def restore(self, memento: "Memento") -> None:
        if memento:
            self.balance = memento.balance
        self.changes.append(memento)
        self.current = len(self.changes) - 1

    def undo(self) -> "Memento":
        memento = None
        if self.current > 0:
            self.current -= 1
            memento = self.changes[self.current]
            self.balance = memento.balance
        return memento

    def redo(self) -> "Memento":
        memento = None
        if self.current + 1 < len(self.changes):
            self.current += 1
            memento = self.changes[self.current]
            self.balance = memento.balance
        return memento

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.undo()
    print(f"Undo 1: {ba}")
    ba.undo()
    print(f"Undo 2: {ba}")
    ba.redo()
    print(f"Redo 1: {ba}")
