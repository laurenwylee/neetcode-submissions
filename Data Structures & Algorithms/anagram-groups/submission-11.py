class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret_val = []
        for x in strs:
            ret_val.append((x, sorted(x)))
        ret_val = sorted(ret_val, key=lambda x: x[1])
        ret = []
        group = []
        curr = ret_val[0][1]
        for x in ret_val:
            if curr == x[1]:
                group.append(x[0])
            else:
                ret.append(group)
                group = []
                group.append(x[0])
            curr = x[1]
        ret.append(group)
        return ret
            
