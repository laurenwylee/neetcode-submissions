class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(numbers):
            if target - n in d:
                return [d[target-n], i + 1]
            d[n] = i + 1
