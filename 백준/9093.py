# 단어 뒤집기
n = int(input())
for _ in range(n):
  line = ''
  stc = input()
  stack = []
  for i in stc:
    if i == " ":
      line += ''.join(stack[::-1])
      line += " "
      stack = []
    else:
      stack.append(i)

  line+=''.join(stack[::-1]) # check
  print(line)

# 마지막에 " " 공백안 만나서 한 단어가 출력 안되는 부분 조심! check 부분