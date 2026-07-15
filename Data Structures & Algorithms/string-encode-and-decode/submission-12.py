class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for i in strs:
            ret = ret + i + "."
        return ret
    def decode(self, s: str) -> List[str]:
        curr = ""
        ret = []
        for i, x in enumerate(s):
            if x == ".":
                ret.append(curr)
                curr = ""
            else:
                curr += x
        return ret