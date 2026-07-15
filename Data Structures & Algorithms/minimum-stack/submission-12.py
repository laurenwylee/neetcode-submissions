class MinStack:

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack == [] or val <= self.minStack[len(self.minStack) - 1]:
            self.minStack.append(val)

    def pop(self) -> None:
        elem = self.stack.pop()
        while self.minStack and elem <= self.minStack[len(self.minStack) - 1]:
            if self.minStack.pop() == elem:
                break
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.minStack[len(self.minStack) - 1]
