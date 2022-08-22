import sys


class Person:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name


class PersonFactory:
    id_count: int = 0

    def create_person(self, name: str) -> Person:
        person = Person(self.id_count, name)
        self.id_count += 1
        return person
        # #код ниже трогать не надо
# names = sys.stdin.read().split(',')
# pf = PersonFactory()
# p1 = pf.create_person(names[0])
# p2 = pf.create_person(names[1])
#
# print(f'{p1.name}:{p1.id};{p2.name}:{p2.id}')
