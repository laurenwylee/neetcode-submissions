class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(i, j):
            while i <= j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        result = []
        curr = []
        def dfs(i, j):
            if i == len(s):
                result.append(curr.copy())
                return
            # either partition or do not partition
            for x in range(i, j):
                if isPalindrome(i, x):
                    curr.append(s[i: x + 1])
                    dfs(x + 1, j)
                    curr.pop()
        dfs(0, len(s))
        return result
        
            