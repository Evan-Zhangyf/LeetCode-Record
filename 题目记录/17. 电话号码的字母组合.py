class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 特判
        if not digits:
            return []
        phone_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ans = []
        def back(number):
            if len(number) == len(digits):
                ans.append(number)
                return
            for i in phone_dict[digits[len(number)]]:
                back(number + i)
        back("")
        return ans