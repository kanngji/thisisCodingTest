# 로또의 최고순위와 최저순위

def solution(lottos, win_nums):
    answer = []
    cnt=0
    # 최고 순위
    for i in lottos:
        if i==0:
            cnt+=1
        for j in win_nums:
            if i==j:
                cnt+=1
    if cnt==6:
        answer.append(1)
    elif cnt==5:
        answer.append(2)
    elif cnt==4:
        answer.append(3)
    elif cnt==3:
        answer.append(4)
    elif cnt==2:
        answer.append(5)
    elif cnt>=0:
        answer.append(6)
    # 최저 순위
    cnt=0
    for i in lottos:
        for j in win_nums:
            if i==j:
                cnt+=1
    if cnt==6:
        answer.append(1)
    elif cnt==5:
        answer.append(2)
    elif cnt==4:
        answer.append(3)
    elif cnt==3:
        answer.append(4)
    elif cnt==2:
        answer.append(5)
    elif cnt>=0:
        answer.append(6)
    return answer