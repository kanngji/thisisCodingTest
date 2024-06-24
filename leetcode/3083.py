class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        reversed_s = s[::-1]
        n = len(s)

        for i in range(n-1):
            if s[i:i+2] in reversed_s:
                return True
        return False