class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        res = []
        res.append([temperatures[0],0])
        for i in range(1, len(temperatures)):
            while res and res[len(res)-1][0] < temperatures[i]:
                elem = res.pop()
                result[elem[1]] = i - elem[1]
            res.append([temperatures[i],i])
        return result

                