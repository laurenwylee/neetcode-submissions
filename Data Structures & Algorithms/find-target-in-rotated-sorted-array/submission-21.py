class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            else:
                # m is on the right side
                if nums[m] < nums[l]:
                    # target definetly on right side
                    if target < nums[m]:
                        r = m - 1
                    # target can be on either side
                    else:
                        # target on right side
                        if target < nums[l]:
                            l = m + 1
                        else:
                            r = m - 1
                # m is on the left side
                else:
                    # target can be on either side
                    if target < nums[m]:
                        # target definetly on right side
                        if target < nums[l]:
                            l = m + 1
                        else:
                            r = m - 1
                    # target definetly on left side
                    else:
                        l = m + 1
        return -1


        
        
        
        
        
        
        
        
        
        
        
        
        
        # l = 0
        # r = len(nums) - 1
        # while l <= r:
        #     print("---")
        #     print(l)
        #     print(r)
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return m
        #     else:
        #         if nums[l] < nums[r]:
        #             if target < nums[m]:
        #                 r = m - 1
        #             else:
        #                 l = m + 1
        #             continue
        #         # either m in the left half or right half
        #         if nums[m] > nums[r]:
        #             # m in left half
        #             if target > nums[m]:
        #                 # target in left half
        #                 l = m + 1
        #             else:
        #                 if target >= nums[l]:
        #                     r = m - 1
        #                 else:
        #                     l = m + 1
        #         else:
        #             # m in right half
        #             if target < nums[m]:
        #                 r = m - 1
        #             else:
        #                 if target > nums[r]:
        #                     r = m - 1
        #                 else:
        #                     l = m + 1
        # return -1


        # l = 0
        # r = len(nums) - 1
        # while l < r:
        #     m = (l + r) // 2
        #     if nums[m] > nums[r]:
        #         l = m + 1
        #     else:
        #         r = m
        # pivot = l
        # print(pivot)
        # if target >= nums[pivot] and target <= nums[len(nums) - 1]:
        #     l = pivot
        #     r = len(nums) - 1
        # else:
        #     l = 0
        #     r = pivot - 1
        # while l <= r:
        #     m = (l + r) // 2
        #     if nums[m] == target:
        #         return m
        #     elif nums[m] < target:
        #         l = m + 1
        #     else:
        #         r = m - 1
        # return -1