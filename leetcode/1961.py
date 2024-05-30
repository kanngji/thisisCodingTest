class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ''
        for i in words:
            res += ''.join(i)
            if res == s:
                return True
        return False