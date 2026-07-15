class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while(l < r):
            p = (l + r) // 2
            if p < len(nums) - 1:
                if nums[p] > nums[p + 1]:
                    print(1)
                    return nums[p+1]
            if p > 0:
                if nums[p] < nums[p-1]:
                    print(2)
                    return nums[p]
            # else:
            if nums[p] > nums[r]:
                l = p + 1
            else:
                r = p - 1
        print(3)
        return nums[l]
            

