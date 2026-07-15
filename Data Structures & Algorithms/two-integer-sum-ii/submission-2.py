class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            if numbers[l] + numbers[r] < target:
                l += 1
        return [min(r, l) +1 , max(r, l)+ 1]