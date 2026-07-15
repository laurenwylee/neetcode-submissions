class Solution:
    def jump(self, nums: List[int]) -> int:
        currEnd = 0
        farthest = 0
        count = 0
        for i in range(len(nums) - 1):   # <-- FIX 1: stop early
            farthest = max(farthest, i + nums[i])

            if i == currEnd:             # <-- when we finish a "layer"
                count += 1
                currEnd = farthest

        return count
        