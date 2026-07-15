class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        exclude_first = nums[1:]
        exclude_last = nums[:-1] #excludes last

        dp_first = [0] * len(exclude_first)
        dp_first[0] = exclude_first[0]
        dp_first[1] = max(exclude_first[1], dp_first[0])
        for i in range(2, len(exclude_first)):
            dp_first[i] = max(exclude_first[i] + dp_first[i-2], dp_first[i-1])

        dp_second = [0] * len(exclude_last)
        dp_second[0] = exclude_last[0]
        dp_second[1] = max(exclude_last[1], dp_second[0])
        for i in range(2, len(exclude_last)):
            dp_second[i] = max(exclude_last[i] + dp_second[i-2], dp_second[i-1])
        
        return max(dp_first[len(exclude_first) - 1], dp_second[len(exclude_last)-1])
