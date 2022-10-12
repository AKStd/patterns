import sys


class Person:
    def __init__(self, age: int):
        self.age = age

    @classmethod
    def drink(cls):
        return 'drinking'

    @classmethod
    def drive(cls):
        return 'driving'

    @classmethod
    def drink_and_drive(cls):
        return 'driving while drunk'


class ResponsiblePerson:
    def __init__(self, person: "Person"):
        self.person = person

    def drink(self) -> str:
        result = "too young"
        if self.person.age >= 18:
            result = self.person.drink()
        return result

    def drive(self) -> str:
        result = "too young"
        if self.person.age >= 16:
            result = self.person.drive()
        return result

    @classmethod
    def drink_and_drive(cls) -> str:
        return 'dead'


# код ниже руками не трогать
age = 10

p = Person(age)
rp = ResponsiblePerson(p)

result = f'{rp.drive()} {rp.drink()} {rp.drink_and_drive()}'
print(result)
