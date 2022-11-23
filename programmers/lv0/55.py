def solution(numbers):
    answer = 0
    numbers.sort()
    gop1=numbers[-1]*numbers[-2]
    gop2=numbers[0]*numbers[1]
    
    if gop1 > gop2:
        answer = gop1
    else:
        answer=gop2
    return answer