class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if self.min == None:
            self.min = val
            self.min_stack.append(val)
        elif self.min >= val:
            self.min = val
            self.min_stack.append(val)
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.stack != []:
            elem = self.stack.pop()
            if elem == self.min:
                self.min_stack.pop()
                if self.min_stack != []:
                   self.min = self.min_stack[len(self.min_stack) - 1]
                else:
                    self.min = None
        
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]
        

    def getMin(self) -> int:
        return self.min
        
