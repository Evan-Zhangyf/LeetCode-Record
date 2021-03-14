class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.content = [0]
        self.keys = [False]


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key > len(self.keys) - 1:
            self.content = self.content + [0] * (key - len(self.content) + 1)
            self.keys = self.keys + [False] * (key - len(self.keys) + 1)
        self.keys[key] = True
        self.content[key] = value


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key > len(self.keys) - 1 or self.keys[key] == False:
            return -1
        else:
            return self.content[key]


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key <= len(self.keys) - 1 and self.keys[key]:
            self.keys[key] = False



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)