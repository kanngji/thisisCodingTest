# 괄호 회전하기

from collections import deque
def solution(s):
    result=0
    dq=deque(s)
    for _ in range(len(dq)):
        cnt=0
        for i in dq:
            if cnt<0:
                break
            if i=='[' or i=='(' or i=='{':
                cnt+=1
            else:
                cnt-=1
        if cnt==0:
            result+=1
        dq.append(dq.popleft())
    
    return result

# TC 3번 실패
# [)(]
def solution(s):
    answer = 0
    temp = list(s)
    
    for _ in range(len(s)):
        st=[]
        for i in range(len(temp)):
            if len(st)>0:
                if st[-1]=='[' and temp[i]==']':
                    st.pop()
                elif st[-1]=='(' and temp[i]==')':
                    st.pop()
                elif st[-1]=='{' and temp[i] == '}':
                    st.pop()
                else:
                    st.append(temp[i])
            else:
                st.append(temp[i])
        if len(st)==0:
            answer+=1
        temp.append(temp.pop(0)) # 첫번쨰 원소를 날리고 제일 끝으로 추가 
    return answer