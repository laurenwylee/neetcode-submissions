class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        subset = []
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
            
        def dfs(i, j):
            if j > len(s):
                return
            if isPalindrome(s[i:j]):
                subset.append(s[i:j])
                if j == len(s):
                    ret.append(subset.copy())
                dfs(j, j + 1)
                subset.pop()
            dfs(i, j + 1)
        dfs(0, 1)
        return ret
