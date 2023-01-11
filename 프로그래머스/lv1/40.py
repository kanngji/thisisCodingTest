# 완주하지 못한 선수

def solution(participant, completion):
    d={}
    for x in participant:
        d[x] = d.get(x,0)+1 # key 값에 x가 없으면 0을 리턴
    for x in completion:
        d[x] -=1
    dnf = [k for k,v in d.items() if v >0] # 완주못한 사람은 value 값이 0 이 아니게 된다
    answer = dnf[0]
    return answer