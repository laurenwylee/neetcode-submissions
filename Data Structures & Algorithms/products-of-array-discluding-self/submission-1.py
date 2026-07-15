class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        # compute prefix first
        res[0] = 1
        for x in range(0, len(nums)-1):
            res[x+1] = res[x] * nums[x]
        print(res)
        # computer postfix second
        postfix = 1
        for x in range(len(nums) - 1, -1, -1):
            res[x] *= postfix
            postfix *= nums[x]
        return res