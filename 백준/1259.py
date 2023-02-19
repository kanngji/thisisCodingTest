# 펠린드롬수
while True:
  cmd=input()
  if cmd=='0':
    break
  elif cmd==cmd[::-1]:
    print("yes")
  else:
    print("no")

