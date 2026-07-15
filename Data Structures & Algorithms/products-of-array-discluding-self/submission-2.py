class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 1
        prefix = [1] * len(nums)
        while i < len(nums):
            prefix[i] = nums[i - 1] * prefix[i - 1]
            i += 1
        suffix = [1] * len(nums)
        i = len(nums) - 2
        while i > -1:
            suffix[i] = nums[i + 1] * suffix[i + 1]
            i -= 1
        print(suffix)
        print(prefix)
        for x in range(len(nums)):
            suffix[x] = suffix[x] * prefix[x]
        return suffix
