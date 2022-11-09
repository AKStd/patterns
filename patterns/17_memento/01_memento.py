class Memento:
    def __init__(self, balance: int) -> None:
        self.balance = balance


class BankAccount:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def deposit(self, amount: int) -> "Memento":
        self.balance += amount
        return Memento(self.balance)

    def restore(self, memento: "Memento") -> None:
        self.balance = memento.balance

    def __str__(self) -> str:
        return f"Balance = {self.balance}"


if __name__ == "__main__":
    ba = BankAccount(100)
    m1 = ba.deposit(50)
    m2 = ba.deposit(25)
    print(ba)

    ba.restore(m1)
    print(ba)

    ba.restore(m2)
    print(ba)
