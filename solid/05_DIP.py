from abc import abstractmethod, ABC
from enum import Enum


class Relation(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipsBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipsBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relation.PARENT, child,)
        )
        self.relations.append(
            (child, Relation.CHILD, parent,)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relation.PARENT:
                yield r[2]


class Research:
    # def __init__(self, _relationships):
    #     relations = _relationships.relations
    #     for r in relations:
    #         if r[0].name == "John" and r[1] == Relationship.PARENT:
    #             print(f'John has child called {r[2].name}')
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f'John has child called {p.name}')


parent = Person("John")
child1 = Person("Cris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
