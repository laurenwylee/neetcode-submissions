class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            d1 = {}
            d2 = {}
            for i in range(len(s)):
                if s[i] in d1.keys():
                    d1[s[i]] = d1[s[i]] + 1
                else:
                    d1[s[i]] = 0
                if t[i] in d2.keys():
                    d2[t[i]] = d2[t[i]] + 1
                else:
                    d2[t[i]] = 0

            if d1 == d2:
                return True
            else:
                return False
        else:
            return False
        