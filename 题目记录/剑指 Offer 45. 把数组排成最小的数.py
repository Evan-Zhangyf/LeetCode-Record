class Solution:
    def minNumber(self, nums: List[int]) -> str:
        # 熟悉sort key的用法，利用python自带的排序修改排序规则（参考了答案）
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        
        ans = [str(num) for num in nums]
        ans.sort(key = functools.cmp_to_key(sort_rule))
        return ''.join(ans)