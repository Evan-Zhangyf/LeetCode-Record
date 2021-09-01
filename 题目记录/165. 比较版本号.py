class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        if len(v1) > len(v2):
            long_version = v1
            ans = 1
        else:
            long_version = v2
            ans = -1
        for i in range(len(long_version)):
            if i < min(len(v1), len(v2)):
                if int(v1[i]) > int(v2[i]):
                    return 1
                if int(v1[i]) < int(v2[i]):
                    return -1
            else:
                if int(long_version[i]) > 0:
                    return ans
        return 0