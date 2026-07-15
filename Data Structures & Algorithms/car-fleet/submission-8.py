class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = []
        for i in range(len(position)):
            ps.append((position[i], speed[i]))
        ps.sort(reverse=True)
        time = []
        for p, s in ps:
            t = (target - p) / s
            time.append(t)
        stack = []
        for x in time:
            if len(stack) == 0 or x > stack[-1]:
                stack.append(x)
        return len(stack)
        
            
                     
