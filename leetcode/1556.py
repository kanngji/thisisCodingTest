class Solution:
    def thousandSeparator(self, n: int) -> str:
        stringn = str(n)
        l = len(stringn)
        if l < 4:
            return stringn

        res = ""
        stringn = stringn[::-1]
        for i in range(l):
            if not i % 3 and i != 0:
                res+="."
            res += stringn[i]
        return res[::-1]