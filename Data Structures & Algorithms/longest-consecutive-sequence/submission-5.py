class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        cter = 1
        before = -1
        potential = []
        nums.sort()
        print(nums)
        for curr in range(len(nums)):
            if before != -1:
                print(nums[curr])
                print(nums[before])
                if nums[curr] - nums[before] == 1:
                    cter += 1
                elif nums[curr] == nums[before]:
                    continue
                else:
                    if cter > 0:
                        potential.append(cter)
                        cter = 1
            before = curr
        potential.append(cter)
        potential.sort()
        print(potential)
        return potential[len(potential) - 1]
        