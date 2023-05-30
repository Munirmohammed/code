class MyHashSet:

    def __init__(self):
        self.x = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.x.append(key)

    def remove(self, key: int) -> None:
        for i in range(len(self.x)):
            if self.x[i] == key:
                self.x.pop(i)
                break

    def contains(self, key: int) -> bool:
        if key in self.x:
            return True
        else:
            return False