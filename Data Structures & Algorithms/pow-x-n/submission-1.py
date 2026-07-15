class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        elif n == - 1:
            return 1/x
        elif n == 0:
            return 1
        else:
            if n % 2 > 0:
                return self.myPow(x, int(n // 2)) * self.myPow(x, int(n // 2)) * self.myPow(x,1)
            else:
                return self.myPow(x, int(n // 2)) * self.myPow(x, int(n // 2))
    