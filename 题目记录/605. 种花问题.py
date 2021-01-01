class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cur = -1
        max_flower = 0
        for i in flowerbed:
            if i == 0:
                cur += 1
            else:
                max_flower += (cur + 1) // 2
                cur = -2
        cur += 1
        max_flower += (cur + 1) // 2
        return max_flower >= n