class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = defaultdict(int)
        for char in t:
            t_dict[char] += 1
        
        l = 0
        r = 0
        s_dict = defaultdict(int)
        min_window = math.inf
        min_idx = None
        while r < len(s):
            if s[r] in t_dict:
                s_dict[s[r]] += 1
            match = True
            for char in t_dict:
                if t_dict[char] > s_dict[char]:
                    match = False
            while l < r and (s[l] not in t_dict or s_dict[s[l]] - 1 >= t_dict[s[l]]):
                    if s[l] in s_dict:
                        s_dict[s[l]] -= 1
                    l += 1
            if match:
                if min_window > r - l + 1:
                    min_window = r - l + 1
                    min_idx = (l, r)
                s_dict[s[l]] -= 1
                l += 1
            r += 1
        if min_idx == None:
            return ""
        return s[min_idx[0]:min_idx[1] + 1]


                