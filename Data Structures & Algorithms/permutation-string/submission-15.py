class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1c = [0] * 26
        s2c = [0] * 26

        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord('a')] += 1
            s2c[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if s1c[i] == s2c[i]:
                matches += 1
        
        l = 1
        r = len(s1)
        while r < len(s2):
            if matches == 26:
                return True
            if s2c[ord(s2[l-1]) - ord("a")] == s1c[ord(s2[l-1]) - ord("a")]:
                matches -= 1
            s2c[ord(s2[l-1]) - ord("a")] -= 1
            if s2c[ord(s2[l-1]) - ord("a")] == s1c[ord(s2[l-1]) - ord("a")]:
                matches += 1
            if s2c[ord(s2[r]) - ord("a")] == s1c[ord(s2[r]) - ord("a")]:
                matches -= 1
            s2c[ord(s2[r]) - ord("a")] += 1
            if s2c[ord(s2[r]) - ord("a")] == s1c[ord(s2[r]) - ord("a")]:
                matches += 1
            
            l+=1
            r+=1
            print(matches)
        if matches == 26:
            return True
        return False
