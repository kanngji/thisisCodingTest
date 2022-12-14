def solution(my_string):
    answer = 0
    flag="plus"
    my_string=my_string.split()
    for i in my_string:
        if i=="+":
            flag="plus"
            continue
        if i=="-":
            flag="minus"
            continue
        if flag=="plus" and i.isdigit():
            answer+=int(i)
        
        if flag=="minus" and i.isdigit():
            answer-=int(i)
        
    return answer