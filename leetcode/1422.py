class Solution:
    def maxScore(self, s: str) -> int:
        l = len(s)-1
        ans = []
        i = 0
        while i<l:
            zcnt = 0
            ocnt = 0
            zcnt = s[:i+1].count('0')
            ocnt=s[l:i:-1].count('1')
            i+=1
            ans.append(zcnt+ocnt)

        return max(ans)