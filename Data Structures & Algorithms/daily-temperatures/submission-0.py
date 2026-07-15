class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        for l in range(len(temperatures)):
            r = l+1
            while r < len(temperatures):
                if temperatures[r] > temperatures[l]:
                    res[l] = r - l
                    break
                else:
                    r += 1
        return res