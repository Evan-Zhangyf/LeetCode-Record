class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt = defaultdict(int)
        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
            else:
                cnt[secret[i]] += 1
        for i in range(len(guess)):
            if guess[i] != secret[i] and cnt[guess[i]] > 0:
                cnt[guess[i]] -= 1
                b += 1
        return str(a) + "A" + str(b) + "B"