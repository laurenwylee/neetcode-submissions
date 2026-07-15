class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            tmp = [0] * 26
            for x in s:
                print(ord(x) - 65)
                tmp[ord(x) - 97] += 1
            d[tuple(tmp)].append(s)
        return list(d.values())
