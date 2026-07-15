class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2) and s1 == s2:
            return True

        s1_dict = {}
        for char in s1:
            if char not in s1_dict:
                s1_dict[char] = 1
            else:
                s1_dict[char] += 1
        
        l = 0
        r = len(s1) - 1
        s2_dict = {}
        for i in range(l, r + 1):
            if s2[i] not in s2_dict:
                s2_dict[s2[i]] = 1
            else:
                s2_dict[s2[i]] += 1
        if s2_dict == s1_dict:
            return True
        r += 1
        l += 1
        while r < len(s2):
            print("===============")
            print(s1_dict)
            print(s2_dict)
            if s2[r] not in s2_dict:
                s2_dict[s2[r]] = 1
            else:
                s2_dict[s2[r]] += 1
            if s2_dict[s2[l - 1]] == 1:
                del s2_dict[s2[l-1]]
            else:
                s2_dict[s2[l - 1]] -= 1
            if s2_dict == s1_dict:
                return True
            l += 1
            r += 1
        return False







