# 올바른 괄호

def solution(s):
    answer = True
    left=0
    right=0
    if s[0]==")":
        answer =False
        return answer
    else:
        for i in s:
            if right>left:
                answer=False
                return answer
            if i=="(":
                left+=1
            else:
                right+=1
        
    if right!=left:
        answer=False
    return answer