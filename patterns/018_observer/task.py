import sys


class Game:
    def __init__(self) -> None:
        ...


class Rat:
    def __init__(self, _game: Game) -> None:
        self.game = _game
        self._attack = 1

    @property
    def attack(self) -> int:
        return len(rats)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...


rats_count = int(sys.stdin.read())
game = Game()
result = ''
rats = []
for x in range(rats_count):
    rat = None
    if x < 2:
        rat = Rat(game)
        rats.append(rat)
    else:
        with Rat(game) as rat3:
            rats.append(rat3)
            for r in rats:
                result += f'{r.attack} '
            rats.pop()
    for r in rats:
        result += f'{r.attack} '

print(result)
