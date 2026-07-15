class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        total = 0
        globalMax = nums[0]
        globalMin = nums[0]

        for n in nums:
            currMax = max(currMax + n, n)
            currMin = min(currMin + n, n)
            globalMax = max(currMax, globalMax)
            globalMin = min(currMin, globalMin)
            total += n

        if globalMax < 0:
            return globalMax

        return max(total - globalMin, globalMax)
                