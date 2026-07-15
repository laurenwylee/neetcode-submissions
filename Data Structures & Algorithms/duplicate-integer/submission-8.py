class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                return True
        return False