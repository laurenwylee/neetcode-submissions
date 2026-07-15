class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r - l) // 2
            if nums[mid] > nums[l]:
                l = mid + 1
            elif nums[mid] < nums[l]:
                r = mid
            else:
                return min(nums[l], nums[r])
        return min(nums[l], nums[r])