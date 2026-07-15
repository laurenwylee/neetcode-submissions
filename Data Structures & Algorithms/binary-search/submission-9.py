class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(l, r):
            mid = (r + (r - l)) // 2
            if nums[mid] == target:
                return mid
            if l >= r:
                return -1
            if nums[mid] < target:
                return binarySearch(mid + 1, r)
            if nums[mid] > target:
                return binarySearch(l, mid - 1)

        return binarySearch(0, len(nums) - 1)
        # l = 0
        # r = len(nums) - 1
        # mid = (r + (r - l)) // 2
        # while l <= r:
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] < target:
        #         l = mid + 1
        #     else:
        #         r = mid - 1
        #     mid = (r + (r - l)) // 2
        # return -1


