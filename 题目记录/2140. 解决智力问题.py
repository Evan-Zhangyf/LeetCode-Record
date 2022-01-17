class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        if len(questions) == 1:
            return questions[0][0]
        dp = [0] * len(questions)
        dp[-1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            if i + questions[i][1] + 1 < len(questions):
                dp[i] = max(dp[i + questions[i][1] + 1] + questions[i][0], dp[i+1])
            else:
                dp[i] = max(questions[i][0], dp[i+1])
        return dp[0]