def solution(absolutes, signs):
    answer = 0
    
    # 파이썬 zip 내장함수로 데이터 엮기
    for pair in zip(absolutes,signs):
        if pair[1]==True:
            answer+=pair[0]
        else:
            answer-=pair[0]
    return answer