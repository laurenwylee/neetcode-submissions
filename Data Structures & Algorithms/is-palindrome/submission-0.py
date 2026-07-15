class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(char for char in s if char.isalnum())
        if len(s) % 2 != 1:
            for x in range(0, int(len(s) / 2)):
                print(s[x])
                print(s[len(s) - 1 - x])
                if s[x] != s[len(s) - 1 - x]:
                    return False
        else:
            for x in range(0, int((len(s) / 2)) + 1):
                if s[x] != s[len(s) - 1 - x]:
                    return False
        return True