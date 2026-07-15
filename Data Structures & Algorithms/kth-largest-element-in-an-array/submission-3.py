class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]
            
            if p == target:
                return nums[p]
            if p > target:
                return quickSelect(l, p - 1)
            if p < target:
                return quickSelect(p + 1, r)
        return quickSelect(0, len(nums)-1)