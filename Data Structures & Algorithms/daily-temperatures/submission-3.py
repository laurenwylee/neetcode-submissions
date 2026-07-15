class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for i in range(len(temperatures)):
            if stack == []:
                stack.append((temperatures[i], i))
            else:
                while stack != [] and temperatures[i] > stack[-1][0]:
                    _, idx = stack.pop()
                    temperatures[idx] = i - idx
                stack.append((temperatures[i], i))
        while stack != []:
            _, idx = stack.pop()
            temperatures[idx] = 0

        return temperatures
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        result = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
            stack.append([t, i])
        return result