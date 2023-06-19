bar = list(input())
answer = 0
stack = []

for i in range(len(bar)):
    if bar[i]=='(': # 스택에 넣기
        stack.append('(')
    else:
        if bar[i-1] == '(': # ()라면 (를 pop하고 현재 스택에 들어있는 ( 수만큼 더함
            stack.pop()
            answer+=len(stack)
        else:
            stack.pop()
            answer+=1 # 끄트머리 막대기 부분을 더해준다
print(answer)