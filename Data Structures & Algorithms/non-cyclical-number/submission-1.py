class Solution:
    def isHappy(self, n: int) -> bool:
        d = {}
        d[n] = True
        while n != 1:
            s = 0
            while n >= 10:
                print(n)
                s += ((n % 10) ** 2)
                n = n // 10
            s += (n ** 2)
            if s in d:
                return False
            else:
                d[s] = True
            n = s
        return True
        