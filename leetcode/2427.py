class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        c = min(a,b)
        cnt = 1

        for i in range(2,c+1):
            if a%i==0 and b%i==0:
                cnt+=1
        return cnt
        
    