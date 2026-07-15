class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[len(nums) - 1]:
            return nums[0]
        l = 0
        r = len(nums) - 1
        minimum = nums[r]
        while l <= r:
            mid = (l + r) // 2
            minimum = min(minimum, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return minimum
            
