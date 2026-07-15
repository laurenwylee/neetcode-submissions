class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slower = 0
        while True:
            slow = nums[slow]
            slower = nums[slower]
            if slow == slower:
                return slow