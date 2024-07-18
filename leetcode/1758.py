class Solution:
    def minOperations(self, s: str) -> int:
        # 패턴1: 010101...
        pattern1 = '0'
        # 패턴2: 101010...
        pattern2 = '1'
        
        # 패턴 길이를 문자열 길이와 동일하게 맞춤
        for i in range(1, len(s)):
            if i % 2 == 0:
                pattern1 += '0'
                pattern2 += '1'
            else:
                pattern1 += '1'
                pattern2 += '0'
        
        # 패턴1과의 차이 계산
        diff1 = sum(1 for i in range(len(s)) if s[i] != pattern1[i])
        # 패턴2와의 차이 계산
        diff2 = sum(1 for i in range(len(s)) if s[i] != pattern2[i])
        
        # 더 작은 값을 반환
        return min(diff1, diff2)