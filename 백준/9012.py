# 괄호

n = int(input())

for _ in range(n):
  leftcnt = 0
  rightcnt = 0
  stc = input()
  flag = True
  for i in range(len(stc)):
    if stc[0] == ')':
      
      flag=False
      break
    else:  # 처음에 ( 일때
      if rightcnt > leftcnt:
        
        flag = False
        break
      if stc[i] == '(':
        leftcnt += 1
      elif stc[i] == ')':
        rightcnt += 1
  if leftcnt == rightcnt and flag == True:
    print("YES")
  if flag==False or leftcnt!=rightcnt:
    print("NO")
  
# TC는 다 맞췃는데 반례를 못ㅂ맞춰서 쏠 못함 
# 예전에는 맞췃는데 하...