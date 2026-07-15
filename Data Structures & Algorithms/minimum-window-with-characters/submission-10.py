class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        ret = sys.maxsize
        t_dict = {}
        s_dict = {}
        idx = [0,0]
        done = 0
        for i in t:
            t_dict[i] = t_dict.get(i, 0) + 1
        if s[r] in t_dict:
            s_dict[s[r]] = s_dict.get(s[r], 0) + 1
            if s_dict[s[r]] == t_dict[s[r]]:
                done += 1
        while r < len(s):
            if done == len(t_dict):
                if ret > r - l + 1:
                    ret = r-l + 1
                    idx = [l,r+1]
                if s[l] in s_dict:
                    if s_dict[s[l]] == t_dict[s[l]]:
                        done -= 1
                    s_dict[s[l]] = s_dict[s[l]] - 1
                    if s_dict[s[l]] == 0:
                        del s_dict[s[l]]
                l += 1
            else:
                r += 1
                if r < len(s) and s[r] in t_dict:
                    s_dict[s[r]] = s_dict.get(s[r], 0) + 1
                    if s_dict[s[r]] == t_dict[s[r]]:
                        done += 1
        return s[idx[0]:idx[1]]
