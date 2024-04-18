class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        n = bin(n)
        n = str(n)
        n = n[2:]
        for i in n:
            if i=='1':
                cnt+=1
        return cnt