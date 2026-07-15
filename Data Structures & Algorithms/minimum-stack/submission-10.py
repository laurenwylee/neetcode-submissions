class MinStack:

    def __init__(self):
        self.stack = []
        self.mstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mstack) == 0:
            self.mstack.append(val)
        else:
            if self.mstack[len(self.mstack) - 1] >= val:
                self.mstack.append(val)

    def pop(self) -> None:
        elem = self.stack[len(self.stack) - 1]
        self.stack = self.stack[0: len(self.stack) - 1]
        if elem == self.mstack[len(self.mstack) - 1]:
            self.mstack = self.mstack[0: len(self.mstack) - 1]


    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.mstack[len(self.mstack) - 1]
