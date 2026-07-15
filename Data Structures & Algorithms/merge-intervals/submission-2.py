class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(interval[0] for interval in intervals)
        mp = [-1] * (max_start + 1)
        for start, end in intervals:
            mp[start] = max(end, mp[start])
        # print(mp)
        ret = []
        largest = -1
        curr = 0
        for s, e in enumerate(mp):
            if e == -1:
                continue
            if largest == -1:
                largest = e
                curr = s
            if s <= largest:
                largest = max(largest, e)
            elif s > largest:
                ret.append((curr, largest))
                largest = e
                curr = s
        ret.append((curr, largest))
        return ret
