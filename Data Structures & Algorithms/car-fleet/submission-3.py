class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(key=lambda i: i[0], reverse = True)
        for i in range(len(cars)):
            reach = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append(reach)
            else:
                if stack[-1] < reach:
                    stack.append(reach)
        return len(stack)