class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= goal:
                goal = 1
            else:
                goal += 1
        if goal > 1:
            return False
        return True
            
        # if len(nums) == 1:
        #     return True
        # max_jump = nums[0]
        # for x in range(1, max_jump + 1):
        #     if self.canJump(nums[x:len(nums)]):
        #         return True
        # return False