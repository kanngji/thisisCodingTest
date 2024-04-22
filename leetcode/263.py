class Solution:
    def isUgly(self, n: int) -> bool:
        if n==1:
            return True
        
        while(n!=1):
            if n%2==0:
                n//=2
            elif n%3==0:
                n//=3
            elif n%5==0:
                n//=5
            else:
                return False
        return True
        
# 시간 초과 이슈
class Solution:
    def isUgly(self, n: int) -> bool:
        if n<= 0: #0 또는 음수인 경우 False 반환
            return False
        for prime in [2,3,5]:
            while n%prime ==0:
                n//=prime
        return n==1    
    
# test ex가 음수 있을 경우 예외처리 잘하기
    
    