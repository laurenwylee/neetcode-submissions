class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        moved = 0
        start = 0
        while moved < n:
            curr = start
            temp = nums[curr]
            while True:
                nxt = (curr + k) % n
                nums[nxt], temp = temp, nums[nxt]
                curr = nxt
                moved += 1
                if curr == start:
                    break
            start += 1