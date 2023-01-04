# 짝지어 제거하기

def solution(s):
    answer = -1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    stack=[]
    for i in s:
        if len(stack)==0:
            stack.append(i)
        
        elif stack[-1]!=i:
            stack.append(i)
        else:
            stack.append(i)
            stack.pop()
            stack.pop()
    if len(stack)==0:
        answer= 1
    else:
        answer=0
    return answer