class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total = len(nums) / 3
        ret_val = []
        curr = []
        check = list(nums)
        for x in range(len(nums)):
            for i in range(x + 1, len(nums)):
                for j in range(i + 1, len(nums)):
                    if nums[x] + nums[i] + nums[j] == 0:
                        curr = [nums[x], nums[i], nums[j]]
                        curr.sort()
                        if curr not in ret_val:
                            ret_val.append(curr)
        return ret_val
