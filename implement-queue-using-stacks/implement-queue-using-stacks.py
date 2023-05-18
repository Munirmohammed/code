class MyQueue:

    def __init__(self):
        self.Stack = []

    def push(self, x: int) -> None:
        return self.Stack.append(x)

    def pop(self) -> int:
        p = self.Stack[0]
        self.Stack = self.Stack[1:]
        return p

    def peek(self) -> int:
        p = self.Stack[0]
        return p

    def empty(self) -> bool:
        if len(self.Stack) == 0:
            return True
        return False