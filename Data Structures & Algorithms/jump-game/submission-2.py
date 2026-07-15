class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= goal:
                goal = 1
            else:
                goal += 1
        if goal > 1:
            return False
        return True

            