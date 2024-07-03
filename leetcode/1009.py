class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n = bin(n)
        n = n[2::]

        n = n.translate(str.maketrans('01','10'))
        n = int(n,2)
        return n
        