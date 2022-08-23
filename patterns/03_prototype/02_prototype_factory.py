import copy


class Address:
    def __init__(self, street_address: str, city: str, suite: int) -> None:
        self.street_address = street_address
        self.city = city
        self.suite = suite

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.suite}'


class Employee:
    def __init__(self, name: str, address: Address) -> None:
        self.name = name
        self.address = address

    def __str__(self) -> str:
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('123 East Dr', 'London', 0))
    aux_office_employee = Employee('', Address('123B East Dr', 'London', 0))

    @staticmethod
    def __new_employee(prototype: Employee, name: str, suite: int) -> Employee:
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name: str, suite: int) -> Employee:
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name: str, suite: int) -> Employee:
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


john = EmployeeFactory.new_main_office_employee('John', 101)
jane = EmployeeFactory.new_aux_office_employee('Jane', 123)

print(john)
print(jane)
