class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0
        while i < len(nums) - 1:
            maxlen = min(nums[i], len(nums) - 1 - i)
            maxjump = -1
            jumpidx = -1
            for j in range(1, maxlen + 1):
                if i + j >= len(nums) - 1:         
                    return count + 1
                if i + j + nums[i + j] >= maxjump:
                    maxjump = i + j + nums[i + j]
                    jumpidx = j
            i += jumpidx
            if i == len(nums) - 1:
                return count + 1
            count += 1
        return count
        
