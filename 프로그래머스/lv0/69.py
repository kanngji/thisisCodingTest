def solution(chicken):
    answer = 0
    res=0
    coupons = chicken
    while(coupons>=10):
        answer+=coupons//10
        coupons=(coupons//10)+(coupons%10)
    
    return answer

# coupons%10 해준 것도 + 해줘야 깔끔하게 된다.