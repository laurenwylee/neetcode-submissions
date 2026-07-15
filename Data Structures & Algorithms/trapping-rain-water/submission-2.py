class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l = 0
        r = len(height) - 1
        ml = height[l]
        mr = height[r]
        sum = 0
        while l < r:
            if ml <= mr:
                l += 1
                ml = max(ml, height[l])
                sum += ml - height[l]
            else:
                r -= 1
                mr = max(mr, height[r])
                sum += mr - height[r]
        return sum