class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bigdict = defaultdict(list) #bigger dict
        for x in strs:
            smalldict = [0] * 26
            for i in x:
                smalldict[ord(i) - 96] += 1
            bigdict[tuple(smalldict)].append(x) 
        retval = []
        for x in bigdict:
            retval.append(bigdict[x])
        return retval
        