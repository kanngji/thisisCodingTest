def solution(rank, attendance):
    dict1={}
    answer = []
    for idx,val in enumerate(rank):
        if attendance[idx]==True:
            dict1[idx]=val
            
    # 해시의 키와 값 쌍을 튜플로 변환, 정렬하기 위해 리스트
    answer = list(dict1.items())
    # 정렬하기 위해 리스트
    res=sorted(answer,key=lambda x:x[1])
    print(res[0][0],res[1][0],res[2][0])
    return res[0][0]*10000+res[1][0]*100+res[2][0]