class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_d = {}
        s2_d = {}
        for i in range(len(s1)):
            s1_d[s1[i]] = 1 + s1_d.get(s1[i], 0)
            s2_d[s2[i]] = 1 + s2_d.get(s2[i], 0)
        
        if s1_d == s2_d:
            return True

        l = 0
        for i in range(len(s1), len(s2)):
            s2_d[s2[i]] = 1 + s2_d.get(s2[i], 0)
            s2_d[s2[l]] -= 1
            if s2_d[s2[l]] == 0:
                del s2_d[s2[l]]
            if s1_d == s2_d:
                return True
            l += 1
        return False

        