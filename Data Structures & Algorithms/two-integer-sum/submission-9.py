class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret = []
        d = {}
        for (i, x) in enumerate(nums):
            if target - x in d:
                ret.append(d[target-x])
                ret.append(i)
            d[x] = i
        return ret