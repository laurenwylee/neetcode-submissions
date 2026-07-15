class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        sets = self.subsets(nums[:-1])
        leng = len(sets)
        for x in range(leng):
            sets.append(sets[x] + [nums[-1]])
        return sets