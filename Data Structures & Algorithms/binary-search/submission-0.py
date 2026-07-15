class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bin_search( l, r, arr, target):
            if l > r:
                return -1
            pivot = (r + l) // 2
            if arr[pivot] == target:
                return pivot
            elif arr[pivot] < target:
                return bin_search( pivot + 1, r, arr, target)
            else:
                return bin_search( 0, pivot - 1, arr, target)
        return bin_search( 0, len(nums) - 1, nums, target)
