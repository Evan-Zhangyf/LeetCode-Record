class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def encode(w):
            ret = 0
            for i in range(len(w)):
                ret += 1 << (ord(w[i]) - ord('a'))
            return ret
        
        def check(s, target):
            target_encode = encode(target)
            for i in range(len(target)):
                if target_encode - (1 << (ord(target[i]) - ord('a'))) in s:
                    return True
            return False
        
        s = set()
        ans = 0
        for w in startWords:
            s.add(encode(w))
        for w in targetWords:
            if check(s, w):
                ans += 1
        return ans
