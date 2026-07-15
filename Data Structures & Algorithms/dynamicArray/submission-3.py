class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.sz = 0
        self.arr = [None] * capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.arr[self.getSize()] = n
        self.sz += 1


    def popback(self) -> int:
        self.sz -= 1
        return self.arr.pop(self.sz)

    def resize(self) -> None:
        og_cap = self.getCapacity()
        self.capacity *= 2
        for x in range(og_cap, self.getCapacity()):
            self.arr.append(None)


    def getSize(self) -> int:
        return self.sz
        
    
    def getCapacity(self) -> int:
        return self.capacity
