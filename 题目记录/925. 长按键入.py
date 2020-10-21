class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ptr1 = 0
        ptr2 = 0
        if name[ptr1] != typed[ptr2]:
            return False
        while ptr1 != len(name):
            if ptr2 == len(typed):
                return False
            while name[ptr1] != typed[ptr2]:
                ptr2 += 1
                if ptr2 == len(typed) or (name[ptr1] != typed[ptr2] and typed[ptr2] != typed[ptr2-1]):
                    return False
            ptr1 += 1
            ptr2 += 1
        for i in range(ptr2, len(typed)):
            if typed[i] != typed[ptr2]:
                return False
        return True