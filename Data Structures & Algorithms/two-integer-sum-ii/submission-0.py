class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        sum = numbers[left] + numbers[right]
        while sum != target:
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
            sum = numbers[left] + numbers[right]
        return [left + 1, right + 1]

        