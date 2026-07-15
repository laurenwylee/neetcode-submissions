class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            p = (l + r) // 2
            # in the left segment
            if nums[p] > nums[r]:
                l = p + 1
            # in the right segment
            else:
                r = p - 1
        pivot = l
        print(pivot)
        if nums[pivot] == target:
            return pivot
        # target is in left of pivot
        if target > nums[len(nums) - 1]:
            l = 0
            r = pivot
            while l <= r:
                p = (l + r) // 2
                if nums[p] == target:
                    return p
                elif nums[p] > target:
                    r = p - 1
                else:
                    l = p + 1
            return -1
        else:
            l = pivot + 1
            r = len(nums) - 1
            while l <= r:
                p = (l + r) // 2
                if nums[p] == target:
                    return p
                elif nums[p] > target:
                    r = p - 1
                else:
                    l = p + 1
            return -1

