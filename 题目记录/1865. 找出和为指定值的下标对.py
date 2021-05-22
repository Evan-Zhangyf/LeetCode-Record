class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1 = nums1
        self.n2 = nums2
        self.n1_dic = {}
        self.n2_dic = {}
        for i in self.n1:
            if self.n1_dic.get(i) != None:
                self.n1_dic[i] += 1
            else:
                self.n1_dic[i] = 1
        for i in self.n2:
            if self.n2_dic.get(i) != None:
                self.n2_dic[i] += 1
            else:
                self.n2_dic[i] = 1

    def add(self, index: int, val: int) -> None:
        if val != 0:
            self.n2_dic[self.n2[index]] -= 1
        self.n2[index] += val
        if self.n2_dic.get(self.n2[index]) != None:
            self.n2_dic[self.n2[index]] += 1
        else:
            self.n2_dic[self.n2[index]] = 1

    def count(self, tot: int) -> int:
        ans = 0
        if len(self.n1) > len(self.n2):
            n = self.n2
            dic = self.n1_dic
        else:
            n = self.n1
            dic = self.n2_dic
        for i in n:
            if dic.get(tot - i) != None:
                ans += dic[tot - i]
        return ans




# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)