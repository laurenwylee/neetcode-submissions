class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_jump = nums[0]
        for x in range(1, max_jump + 1):
            if self.canJump(nums[x:len(nums)]):
                return True
        return False