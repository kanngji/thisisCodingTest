class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        tmp = ''
        for i in range(len(s)-1,-1,-1):
            if i!=0:
                tmp+=s[i]+' '
            else:
                tmp+=s[i]

        return tmp