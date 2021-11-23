class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        duplicate = False
        diff_cnt = 0
        s_letter = defaultdict(int)
        goal_letter = defaultdict(int)
        for i in range(len(s)):
            s_letter[s[i]] += 1
            goal_letter[goal[i]] += 1
            if s[i] != goal[i]:
                diff_cnt += 1
        for l in s_letter:
            if s_letter[l] != goal_letter[l]:
                return False
            if s_letter[l] > 1:
                duplicate = True
        if (diff_cnt == 0 and duplicate) or diff_cnt == 2:
            return True
        return False