import copy


class Address:
    def __init__(self, street_address: str, city: str, country: str) -> None:
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f"{self.name} lives at {self.address}"


"""
john = Person('John', Address('123 London Road', 'London', 'UK'))
print(john)
# john и jane ссылаются на один и тот же объект
jane = john
jane.name = 'Jane'
print('---------')
print(jane)
print(john)
"""


# copy.deepcopy()
john = Person("John", Address("123 London Road", "London", "UK"))
print(john)

jane = copy.deepcopy(john)
jane.name = "Jane"
print("---------")
print(jane)
print(john)
