class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        for x in t:
            t_dict[x] += 1
        if s_dict == t_dict:
            return True
        else:
            return False