class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if postorder == []:
            return True
        i = 0
        while postorder[i] < postorder[-1]:
            i += 1
        border = i
        while postorder[i] > postorder[-1]:
            i += 1
        return i == len(postorder) - 1 and self.verifyPostorder(postorder[:border]) and self.verifyPostorder(postorder[border:-1])