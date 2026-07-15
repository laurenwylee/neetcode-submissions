class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        elems = {}
        for i, x in enumerate(numbers):
            if target - x in elems:
                return [elems[target - x], i + 1]
            elems[x] = i + 1