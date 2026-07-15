class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        curr = 0
        for x in nums:
            if curr < 0:
                curr = 0
            curr += x
            maximum = max(curr, maximum)
        return maximum