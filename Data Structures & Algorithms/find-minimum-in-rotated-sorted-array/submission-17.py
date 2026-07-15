class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                return nums[l]
            mid = l + (r - l) // 2
            # mid in in the right side
            if nums[mid] < nums[l]:
                r = mid
            # mid in the left side
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:
                return min(nums[l], nums[r])
        return min(nums[l], nums[r])
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # l = 0
        # r = len(nums) - 1
        # lowest = nums[0]
        # while l <= r:
        #     if nums[l] < nums[r]:
        #         lowest = min(lowest, nums[l])
        #         break
        #     m = l + (r - l) // 2
        #     if nums[l] <= nums[m]:
        #         lowest = min(lowest, nums[m])
        #         l = m + 1
        #     else:
        #         r = m
        # return lowest
        # while l < r:
        #     m = l + (r - l) // 2
        #     if nums[m] < nums[r]:
        #         r = m
        #     else:
        #         l = m + 1
        # return nums[l]

           