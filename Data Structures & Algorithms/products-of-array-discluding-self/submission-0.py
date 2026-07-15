class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_val = []
        curr = 1
        if 0 not in nums:
            for i in range(1, len(nums)):
                curr = curr * nums[i]
            ret_val.append(curr)
            for x in range(1, len(nums)):
                curr = curr / nums[x]
                # print(nums[i])
                curr = curr * nums[x - 1]
                # print(curr)
                ret_val.append(int(curr))
        else:
            ret_val = []
            for x in range(0, len(nums)):
                curr = 1
                for i in range(0, len(nums)):
                    if i != x:
                        curr = curr * nums[i]
                ret_val.append(curr)
                
        return ret_val
        