class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isDivisor(l):
            len1 = len(str1)
            len2 = len(str2)
            if len1 % l != 0 or len2 % l != 0:
                return False
            f1 = len1 // l
            f2 = len2 // l

            return f1 * str1[:l] == str1 and f2 * str1[:l] == str2
        for i in range(min(len(str1), len(str2)), 0, -1):
            if isDivisor(i):
                return str1[:i]
        return ""