import sys
from abc import ABC
from enum import Enum


class Game:
    def __init__(self) -> None:
        self.queries = Event()
        self.creatures = []

    def perform_query(self, sender, query):
        self.queries(sender, query)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 2


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Event(list):
    def __call__(self, *args, **kwds):
        for item in self:
            item(*args, **kwds)


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.game = game
        self.creature = creature
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass


class JoinDefenderModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            isinstance(sender, Goblin)
            and sender is not self.creature
            and query.what_to_query == WhatToQuery.DEFENSE
        ):
            query.value += 1


class KingAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if (
            isinstance(sender, Goblin)
            and sender is not self.creature
            and query.what_to_query == WhatToQuery.ATTACK
        ):
            query.value += 1


class Creature:
    def __init__(self, game, name, attack, defense):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perfome_query(self, q)
        return q.value

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perfome_query(self, q)
        return q.value

    def __str__(self) -> str:
        return f"{self.name} ({self.attack}/{self.defense})"


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, "goblin", attack, defense)
        JoinDefenderModifier(game, self)


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)
        KingAttackModifier(game, self)


# код ниже руками не трогать
goblins = sys.stdin.read().split()
result = ""
for g in goblins:
    _game = Game()
    goblin = None
    goblin = Goblin(_game) if g == "g" else GoblinKing(_game)
    _game.creatures.append(goblin)

    result += f"{goblin.attack} {goblin.defense} "

print(result)
