class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ableReach = 0
        i = 0
        for i in range(len(nums)):
            if i <= ableReach:
                ableReach = max(ableReach, i + nums[i])
        if ableReach < len(nums) - 1:
            return False
        return True
