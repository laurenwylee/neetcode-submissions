class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = nums[0]
        curr_total = 0
        for x in nums:
            if curr_total < 0:
                curr_total = x
            else:
                curr_total += x
            m = max(m, curr_total)
        return m