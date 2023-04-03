# 추억 점수

def solution(name, yearning, photo):
    dict1={} # 빈 딕셔너리 생성
    answer = []
    for i in range(len(name)):
        dict1[name[i]]=yearning[i]
        
    for i in photo:
        score=0
        for j in i:
            for key,val in dict1.items():
                if j==key:
                    score+=val
        answer.append(score)
    return answer