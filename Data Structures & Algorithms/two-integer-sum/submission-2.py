class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in d.keys():
                index1 = d[rest]
                index2 = i 
                return [min(index1, index2), max(index1, index2)]
            else:
                d[nums[i]] = i