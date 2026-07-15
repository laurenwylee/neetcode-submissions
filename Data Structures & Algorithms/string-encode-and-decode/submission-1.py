class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_val = ""
        for x in strs:
            ret_val = ret_val + str(x) + "\n"
            print(ret_val)
        return ret_val

    def decode(self, s: str) -> List[str]:
        group = []
        curr = ""
        for x in s:
            if x != "\n":
                curr = curr + x
            else:
                group.append(curr)
                curr = ""
        print(group)
        return group

