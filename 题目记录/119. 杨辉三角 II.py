class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        previous_row = [1]
        for cur_index in range(1, rowIndex + 1):
            cur_row = [1]
            for i in range(cur_index - 1):
                cur_row.append(previous_row[i] + previous_row[i+1])
            cur_row.append(1)
            previous_row = cur_row
        return cur_row