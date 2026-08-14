class ResearchMemory:

    def __init__(self):
        self.memory = {}

    def remember(self, key, value):
        self.memory[key] = value

    def recall(self, key):
        return self.memory.get(key)

    def get_all(self):
        return self.memory

    def clear(self):
        self.memory.clear()