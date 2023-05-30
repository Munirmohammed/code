class MinStack:
    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_values or x <= self.min_values[-1]:
            self.min_values.append(x)

    def pop(self) -> None:
        if self.stack.pop() == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]
