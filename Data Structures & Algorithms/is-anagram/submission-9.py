class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        d2 = {}
        for i in t:
            if i not in d2:
                d2[i] = 1
            else:
                d2[i] += 1
        if d.keys() < d2.keys():
            A = d2
            B = d
        else:
            A = d
            B = d2
        for i in A.keys():
            if i not in B:
                return False
            else:
                if d[i] != d2[i]:
                    return False
        return True
