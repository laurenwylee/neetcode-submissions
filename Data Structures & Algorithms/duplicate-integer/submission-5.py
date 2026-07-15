class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            if x in d.keys():
                return True
            else:
                d[x] = x
        return False