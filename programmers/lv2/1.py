# 최솟값과 최댓값

def solution(s):
    s=s.split(" ")
    # 리스트 안에를 정수로 변환
    s=list(map(int,s))
    # 최소 최대 가르기위한 sort()
    s.sort()
    answer = []
    answer.append(s[0])
    answer.append(s[-1])
    
    answer=' '.join(map(str,answer))
    return answer