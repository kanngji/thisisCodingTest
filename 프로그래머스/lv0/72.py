def solution(my_string):
    answer = 0
    strnum=""
    for i in my_string:
        # i 가 숫자냐 아니냐 판별해주는 함수
        if i.isdigit():
            strnum+=i
        else:
            if strnum!="":
                answer+=int(strnum)
                strnum=""
    # 마지막에 숫자로 끝나는경우도 더해야한다
    if strnum!="":
        answer+=int(strnum)
                
    return answer