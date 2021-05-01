"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sub_sum = 0
        find = {}
        for i in range(len(employees)):
            find[employees[i].id] = i
        def helper(id):
            ret = employees[find[id]].importance
            for i in employees[find[id]].subordinates:
                ret += helper(i)
            return ret
        return helper(id)
