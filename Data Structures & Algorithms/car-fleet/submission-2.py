class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        count = 0
        cars = [(p,s) for p, s in zip(position, speed)]
        cars.sort(key=lambda i: i[0], reverse = True)
        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if stack == []:
                stack.append(time)
            else:
                if stack[-1] < time:
                    stack.append(time)
        return len(stack)