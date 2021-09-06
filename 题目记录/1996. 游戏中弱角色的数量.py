class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x: -x[0])
        max_defense = 0
        cur_atk = properties[0][0]
        tmp_max = 0
        ans = 0
        for i in range(len(properties)):
            if cur_atk != properties[i][0]:
                max_defense = max(max_defense, tmp_max)
                cur_atk = properties[i][0]
                tmp_max = properties[i][1]
            else:
                tmp_max = max(properties[i][1], tmp_max)
            if properties[i][1] < max_defense:
                ans += 1
        return ans