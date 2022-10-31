class Creature:
    def __init__(self, name: str, attack: int, defense: int) -> None:
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self) -> str:
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier:
    def __init__(self, creature: "Creature"):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier: "CreatureModifier"):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling attack of {self.creature.name}")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseFilter:
    @classmethod
    def is_valid(cls, modifier: "CreatureModifier"):
        return modifier.creature.attack <= 2


class IncreaseDefense(CreatureModifier):
    _filter = IncreaseDefenseFilter

    def handle(self):
        if self._filter.is_valid(self):
            print(f"Increasing {self.creature.name} defense")
            self.creature.defense += 1
        else:
            print(f"{self.creature.name} attack is too big!")
        super().handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you!")


if __name__ == "__main__":
    goblin = Creature(name="goblin", attack=1, defense=1)
    print(goblin)

    root = CreatureModifier(goblin)
    root.add_modifier(NoBonusesModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefense(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))
    root.handle()

    print(goblin)
