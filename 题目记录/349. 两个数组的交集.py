class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        ans = []
        for i in nums1:
            if not dic.get(i):
                dic[i] = True
        for i in nums2:
            if dic.get(i):
                ans.append(i)
                dic[i] = False
        return ans