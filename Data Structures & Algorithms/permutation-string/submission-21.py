class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_dict = {}
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        s2_window = {}
        l = 0
        r = len(s1) - 1
        for i in range(l, r + 1):
            if s2[i] not in s2_window:
                s2_window[s2[i]] = 1
            else:
                s2_window[s2[i]] += 1
        if s1_dict == s2_window:
            return True
        l += 1
        r += 1
        while r < len(s2):
            s2_window[s2[l - 1]] -= 1
            if s2_window[s2[l - 1]] == 0:
                del s2_window[s2[l - 1]]
            if s2[r] not in s2_window:
                s2_window[s2[r]] = 1
            else:
                s2_window[s2[r]] += 1
            if s1_dict == s2_window:
                return True
            l += 1
            r += 1
        return False

            
