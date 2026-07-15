class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        firstOccur = {}
        for i in range(len(s)):
            firstOccur[s[i]] = i
        size = 0
        end = -1
        ret = []
        for i in range(len(s)):
            size = max(size, firstOccur[s[i]])
            if size == i:
                ret.append(size - end)
                end = i
                size = 0

        return ret