class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        track = []
        for x in nums:
            if x in track:
                return True
            else:
                track.append(x)
        return False
