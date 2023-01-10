def solution(price):
    answer = 0
    if 100000<=price <300000:
        answer=price*0.95
    elif 300000<=price<500000:
        answer=price*0.9
    elif 500000<=price:
        answer=price*0.8
    
    # 10만원 이하인 경우도 깜빡하지말고
    else:
        answer=price
    answer = int(answer)
    return answer