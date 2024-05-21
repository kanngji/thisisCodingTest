class Solution:
    def countSegments(self, s: str) -> int:

        
        ans = s.split()
        return len(ans)
    

# segments = s.split(' ')
# split(' ') 메서드는 정확히 하나의 스페이스 문자를 구분자로 사용합니다.
# 연속된 스페이스 문자는 빈 문자열을 결과 리스트에 포함시킵니다.


# segments = s.split()
# split() 메서드를 호출할 때 인수를 제공하지 않으면, 기본적으로 모든 종류의 공백(스페이스, 탭, 개행 등)을 구분자로 사용합니다.
# 이 메서드는 연속된 공백을 하나의 구분자로 간주하여 결과 리스트에 빈 문자열이 포함되지 않습니다.