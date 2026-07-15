class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         d = {}
         for i in nums:
            if i not in d:
                d[i] = True
            else:
                return True
         return False