class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        longest= 0 
        for x in nums:
            if x-1 not in d.keys():
                len = 1
                while len+x in nums:
                    len = len + 1
                longest = max(longest, len)
        return longest
                