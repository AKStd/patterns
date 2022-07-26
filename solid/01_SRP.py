# Принцип единой ответственности

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}){text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    """
    # Вторичная ответственность!
    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self))

    # Вторичная ответственность!
    def load(self):
        pass
    """


class PersistenceManager:
    @staticmethod
    def save_to_file(content, filename):
        with open(filename, 'w') as f:
            f.write(str(content))
