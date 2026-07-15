class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        res = []
        sets = self.subsets(nums[:-1])
        for x in sets:
            res.append(x)
            res.append(x + [nums[-1]])
        return res