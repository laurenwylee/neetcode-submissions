class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlength = 0
        for n in numSet:
            length = 1
            i = n-1
            while i in numSet:
                length += 1
                i-=1
            maxlength = max(length, maxlength)

        return maxlength