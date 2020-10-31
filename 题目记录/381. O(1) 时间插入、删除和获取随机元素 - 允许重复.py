class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_list = []
        self.index_dic = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.num_list.append(val)
        if self.index_dic.get(val):
            self.index_dic[val].append(len(self.num_list) - 1)
            return False
        else:
            self.index_dic[val] = [len(self.num_list) - 1]
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if self.index_dic.get(val):
            i = self.index_dic[val][-1]
            if i == len(self.num_list) - 1:
                self.index_dic[val].pop()
                self.num_list.pop()
            else:
                self.num_list[-1], self.num_list[i] = self.num_list[i], self.num_list[-1]
                self.index_dic[val].pop()
                self.index_dic[self.num_list[i]].remove(len(self.num_list)-1)
                self.num_list.pop()
                self.index_dic[self.num_list[i]].append(i)
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        import random
        return random.choice(self.num_list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()