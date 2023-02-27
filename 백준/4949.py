# 균형잡힌 세상

#from collections import deque

while True:
  s = input()
  if s=='.':
    break
  dq = []
  for i in s:
    if i == '[' or i == '(':
      dq.append(i)
    elif i == ']' or i == ')':
      if len(dq)>0:
        
        if i == ']' and dq[-1] == '[':
          dq.pop()
        else:
            dq.append(i)
            break
        
        if i == ')' and dq[-1] == '(':
          dq.pop()
        else:
           dq.append(i)
           break
    elif i == '.':
      break
  if len(dq) != 0:
    print('no')
  else:
    print('yes')

# 예제는 맞는데 틀려서 다른 사람 풀이 참고
while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in a :
        if i == '[' or i == '(' :
            stack.append(i)
        elif i == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop() # 맞으면 지워서 stack을 비워줌 0 = yes
            else : 
                stack.append(']')
                break
        elif i == ')' :
            if len(stack) != 0 and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(')')
                break
    if len(stack) == 0 :
        print('yes')
    else :
        print('no')
