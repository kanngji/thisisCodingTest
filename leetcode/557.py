class Solution:
    def reverseWords(self, s: str) -> str:
        text = s.split()
        ans = []
        for i in text:
            ans.append(i[::-1])

        ans = ' '.join(ans)

        return ans
    
# 리스트 슬라이싱