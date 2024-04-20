class Solution:
    def sortSentence(self, s: str) -> str:
        text = s.split()
        ans = [''] * len(text)
        for i in text:
            n=i[-1]
            ans[int(n)-1] = i[0:-1]

        ans=' '.join(ans)
        return ans
    
    # s.spit()
    # ans = ' '.join(ans)