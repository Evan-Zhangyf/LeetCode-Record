class Solution:
    def maximumTime(self, time: str) -> str:
        ans = list(time)
        if time[0] == "?":
            if time[1] == "?" or time[1] <= "3":
                ans[0] = "2"
            else:
                ans[0] = "1"
        if time[1] == "?":
            if ans[0] == "2":
                ans[1] = "3"
            else:
                ans[1] = "9"
        if time[3] == "?":
            ans[3] = "5"
        if time[4] == "?":
            ans[4] = "9"
        return "".join(ans)