class MyStack:

    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)
        for i in range(len(self.arr)-1):
            self.arr.append(self.arr.pop(0))

    def pop(self) -> int:
        return self.arr.pop(0)

    def top(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        if len(self.arr) == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()