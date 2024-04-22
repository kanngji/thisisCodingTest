class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>1 and n%2==1:
            return False
        if n==1:
            return True
        
        else:
            while (n!=1):
                n=n//2
                if n%2!=0 and n!=1:
                    return False
            return True

# 시간 초과 이슈
        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0: # 음수나 0일 때는 2의 거듭제곱이 아님
            return False
        
        return n & (n-1) == 0
    
#이 코드는 주어진 수와 그 수에서 1을 뺀 값의 비트 AND 연산을 수행하여 결과가 0인지를 확인합니다. 
# 2의 거듭제곱 수는 이진수로 표현했을 때 1 비트가 하나뿐이므로 그 수에서 1을 빼면 그 이전 비트들이 모두 1이 됩니다. 
# 그래서 이를 AND 연산하면 0이 됩니다.
        