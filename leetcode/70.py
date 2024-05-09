class Solution:
    def climbStairs(self, n: int) -> int:
        # DP
        # dp 배열 만들기
        # 1계단 , 2계단 미리 저장
        # 반복문 -> DP테이블 채워주기
        # formular 적용시키기
        # 최종 결과값 리턴하기
        if n == 0 or n==1 :
            return 1
        
        dp = [0 for _ in range(n+1)]

        dp[0] = dp[1] = 1
        dp[2] = 2

        for i in range(3,len(dp)):
            dp[i] = dp[i-1]+ dp[i-2]
        return dp[n]