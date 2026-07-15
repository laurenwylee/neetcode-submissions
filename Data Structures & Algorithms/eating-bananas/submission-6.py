class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        curr = r
        while l <= r:
            mid = l + (r - l) // 2
            ct = 0
            for x in piles:
                ct += math.ceil(x / mid)
            if ct > h:
                l = mid + 1
            else:
                r = mid - 1
                curr = min(curr, mid)
        return curr

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # l = 1
        # r = max(piles)
        # curr = r
        # while l <= r:
        #     mid = l + (r - l) // 2
        #     tot = 0
        #     for x in piles:
        #         tot = tot + math.ceil(x / mid)
        #     print(mid)
        #     print(tot)
        #     print(l)
        #     print(r)
        #     if tot > h :
        #         l = mid + 1
        #     else:
        #         curr = min(curr, mid)
        #         r = mid - 1
        # return curr