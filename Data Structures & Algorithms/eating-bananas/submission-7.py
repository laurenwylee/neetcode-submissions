class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            total = 0
            mid = l + (r - l) // 2
            for p in piles:
                total += math.ceil(p / mid)
            if total > h :
                l = mid + 1
            else:
                r = mid - 1
                res = min(res, mid)
        return res
