class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left = {}
        for x in s:
            if x in left:
                left[x] += 1
            else:
                left[x] = 1
        right = {}
        for x in t:
            if x in right:
                right[x] += 1
            else:
                right[x] = 1
        for x in left:
            if x not in right:
                return False
            if x in right and left[x] != right[x]:
                return False
        for x in right:
            if x not in left:
                return False
            if x in left and left[x] != right[x]:
                return False
        return True
                
        