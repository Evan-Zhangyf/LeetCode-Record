class CQueue:

    def __init__(self):
        self.stack_for_append = []
        self.stack_for_delete = []


    def appendTail(self, value: int) -> None:
        self.stack_for_append.append(value)
        return


    def deleteHead(self) -> int:
        if not self.stack_for_delete:
            while self.stack_for_append:
                tmp = self.stack_for_append.pop()
                self.stack_for_delete.append(tmp)
            if not self.stack_for_delete:
                return -1
        return self.stack_for_delete.pop()



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()