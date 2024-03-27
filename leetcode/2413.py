class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n*2
        
# 양의 정수 n이 주어지면 2와 n의 배수인 가장 작은 양의 정수를 반환합니다.