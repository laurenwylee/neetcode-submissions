class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxNum = float('-inf')
        maxIdx = -1
        l = 0
        r = k - 1
        window = {}
        ret = [-1] * (len(nums) - k + 1)
        for i in range(l, k):
            # if nums[i] in window:
                # count = window[nums[i]][1]
                # window[nums[i]] = [i, count + 1]
            window[nums[i]] = i
            # else:
                # window[nums[i]] = [i, 1]
            if nums[i] >= maxNum:
                maxNum = nums[i]
                maxIdx = i
        while r < len(nums):
            if l > 0 and l - 1 == maxIdx:
                # find new max
                maxNum = float('-inf')
                for i in range(l, r+1):
                    print(l)
                    print(r)
                    if nums[i] >= maxNum:
                        maxNum = nums[i]
                        maxIdx = i
                
            if nums[r] >= maxNum:
                maxNum = nums[r]
                maxIdx = r
            ret[l] = maxNum
            l += 1
            r += 1
            # window[nums[l]][1] -= 1
            # if window[nums[l]][1] == 0:
            #     del window[nums[l]][1]
            # if if l == maxIdx and nums[l] not in window:
            #     for i in window:
            #         if i > maxNum:
            #             maxNum = nums[i]
            #             maxidx = i
        return ret