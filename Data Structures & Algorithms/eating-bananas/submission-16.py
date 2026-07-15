class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = sys.maxsize
        while l <= r:
            mid = (r + l) // 2
            hours = 0
            # print("-----")
            # print(mid)
            for i in piles:
                # print(math.ceil(i // mid))
                hours = hours + (i // mid)
                if i % mid > 0:
                    hours += 1
            if hours <= h:
                # print("Test")
                best = min(best, mid)
                r = mid - 1
            else:
                # print("test")
                l = mid + 1
        return best