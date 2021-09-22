class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dic = defaultdict(int)
        def back(pos, cur_len):
            nonlocal ans
            if pos == len(arr):
                return
            cur = 0
            while cur < len(arr[pos]):
                if dic[arr[pos][cur]] == 0:
                    dic[arr[pos][cur]] += 1
                    cur += 1
                else:
                    for i in range(cur):
                        dic[arr[pos][i]] -= 1
                    break
            if cur == len(arr[pos]):
                ans = max(ans, cur_len + len(arr[pos]))
                back(pos + 1, cur_len + len(arr[pos]))
                for i in range(len(arr[pos])):
                     dic[arr[pos][i]] -= 1
            back(pos + 1, cur_len)

        ans = 0
        back(0, 0)
        return ans