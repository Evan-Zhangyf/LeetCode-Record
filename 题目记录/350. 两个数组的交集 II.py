class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        for i in nums1:
            if hashmap.get(i) == None:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        ans = []

        for i in nums2:
            if hashmap.get(i) != None:
                if hashmap[i] >= 1:
                    hashmap[i] -= 1
                    ans.append(i)
        return ans
