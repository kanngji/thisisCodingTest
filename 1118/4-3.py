# 현재 나이트의 위치 입력받기
# 입력문자는 a1 처럼 열과 행으로 이루어진다

input_data = input()

# row , column 1,1 시작
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a'))+1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0

for step in steps:
  nr = row + step[0]
  nc = column + step[1]
  # 해당 위치로 이동이 가능하다면 카운트 증가
  if nr >= 1 and nr <=8 and nc>=1 and nc<=8:
    result+=1

print(result)