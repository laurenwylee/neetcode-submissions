class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, i in enumerate(nums):
            if target - i in d:
                ret = [idx, d[target-i]]
                ret.sort()
                return ret
            d[i] = idx