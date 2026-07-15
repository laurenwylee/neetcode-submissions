class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_val = ""
        for s in strs:
            ret_val += str(len(s)) + "#" + s
        return ret_val

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(s[i:j])
            leng = int(s[i:j])
            j = j + 1
            i = j + leng
            ret.append(s[j:i])
      
        return ret

