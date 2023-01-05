# 분수의 덧셈

def solution(denum1, num1, denum2, num2):
    # 1.분모끼리 곱한다
    # 2. 분자에 common_mo를 num1, num2 값을 나눈 값을 곱하고 더한다
    
    answer = []
    common_mo = num1 * num2
    denum1 = common_mo // num1 * denum1
    denum2 = common_mo // num2 * denum2
    
    common_ja = denum1 + denum2
    # 약분 해주면 됨
    x=2
    while x<=common_ja and x<=common_mo:
        if common_ja%x==0 and common_mo%x==0:
            common_ja//=x
            common_mo//=x
        else:
            x+=1
        
    answer.append(common_ja)
    answer.append(common_mo)
    return answer