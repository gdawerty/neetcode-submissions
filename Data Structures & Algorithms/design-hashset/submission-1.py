class MyHashSet:

    def __init__(self):
        self.size = 1009
        self.bucket = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        if key not in self.bucket[key % self.size]:
            self.bucket[key % self.size].append(key)
            

    def remove(self, key: int) -> None:
        if key in self.bucket[key % self.size]:
            self.bucket[key % self.size].remove(key)

    def contains(self, key: int) -> bool:
        if key in self.bucket[key % self.size]:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)