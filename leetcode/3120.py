class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        word = [x for x in word]

        upper =[]
        lower = []

        for i in word:
            if i.isupper():
                upper.append(i)
            else:
                lower.append(i)

        upper = list(set(upper))
        lower = list(set(lower))

        lower = [x.upper() for x in lower]

        lower.sort()
        upper.sort()

        for i in lower:
            if i in upper:
                cnt+=1

        return cnt 