class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        total = 0
        min_size = sys.maxsize
        while r < len(nums):
            total += nums[r]
            while l < r and total >= target:
                min_size = min(min_size, r - l + 1)
                total -= nums[l]
                l += 1
            if total >= target:
                min_size = min(min_size, r - l + 1)
            r += 1
        if min_size == sys.maxsize:
            return 0
        return min_size
