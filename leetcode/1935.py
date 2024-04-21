class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a  = text.split()
        cnt = len(a)
        for i in a:
            for j in brokenLetters:
                if j in i:
                    cnt-=1
                    break

        return cnt
            