class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        result = []
        while i < len(nums):
            if i > 0:
                while i < len(nums) and nums[i - 1] == nums[i]:
                    i+=1
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                else:
                    r-=1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
            i+=1
        return result
                
