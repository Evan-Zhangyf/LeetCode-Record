class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.dict.get(key):
            self.dict[key][0].append(value)
            self.dict[key][1].append(timestamp)
        else:
            self.dict[key] = [[value], [timestamp]]


    def get(self, key: str, timestamp: int) -> str:
        if self.dict.get(key):
            if self.dict[key][1][0] > timestamp:
                return ""
            l = 0
            r = len(self.dict[key][1]) - 1
            from math import ceil
            while l < r:
                m = ceil((l + r) / 2)
                if self.dict[key][1][m] > timestamp:
                    r = m - 1
                else:
                    l = m
            return self.dict[key][0][l]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)