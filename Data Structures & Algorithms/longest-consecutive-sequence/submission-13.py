class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = 1
        start = []
        for i in d:
            if i - 1 not in d:
                start.append(i)
        max_sequence = 0
        for i in start:
            count = 1
            j = i
            while j + 1 in d:
                j+=1
                count+=1
            max_sequence = max(count, max_sequence)
        return max_sequence

