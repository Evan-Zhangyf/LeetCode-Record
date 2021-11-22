class Solution:
    from random import randint
    def __init__(self, nums: List[int]):
        self.original = nums
        self.cur = nums[:]

    def reset(self) -> List[int]:
        return self.original

    def shuffle(self) -> List[int]:
        # Knuth shuffle
        for i in range(len(self.cur) - 1, 0, -1):
            rand = randint(0, i)
            self.cur[i], self.cur[rand] = self.cur[rand], self.cur[i]
        return self.cur




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()