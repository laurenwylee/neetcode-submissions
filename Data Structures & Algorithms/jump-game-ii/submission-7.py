class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        steps = 0
        while l < len(nums) and r < len(nums) - 1:
            maximum = l
            for i in range(l, r + 1):
                maximum = max(maximum, nums[i] + i)
            l = r + 1
            r = maximum
            steps += 1
        return steps
