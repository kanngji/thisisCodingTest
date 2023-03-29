# 공원산책

park = ["OSO", "OOO", "OXO", "OOO"]
routes = ["E 2", "S 3", "W 1"]
row = len(park)
col = len(park[0])
x, y = 0, 0
for i in range(row):
  for j in range(col):
    if park[i][j] == 'S':
      x, y = i, j

# N E S W
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
move_types = ['N', 'E', 'S', 'W']
for route in routes:
  dir, box = route.split()
  for i in range(len(move_types)):
    if dir == move_types[i]:
      nx = x + (dx[i] * int(box))
      ny = y + (dy[i] * int(box))
  # 공간을 벗어나는 경우 무시
  if nx < 0 or ny < 0 or nx > row or ny > col:
    continue
  if park[nx][ny] == 'X':

    continue

  else:
    x, y = nx, ny

print(x, y)

# 다른 사람 풀이

dx = {'N':-1, 'S':1, 'E':0, 'W': 0}
dy = {'N': 0, 'S':0, 'E':1, 'W':-1}

def solution(park, routes):
    answer = []
    x, y = -1, -1
    # 시작 지점 S 찾기 ok 
    N, M = len(park), len(park[0])
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                x, y = i, j
    # 방향과 거리 설정 하기 ok
    for route in routes:
        dir_, dist = route.split(' ')

        isFalse = False
        for i in range(1, int(dist) + 1):
            nx, ny = x + dx[dir_] * i, y + dy[dir_] * i
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                isFalse = True
                break
            if park[nx][ny] == 'X':
                isFalse = True
                break

        if isFalse:
            continue
        nx, ny = x + dx[dir_] * int(dist), y + dy[dir_] * int(dist)
        x, y = nx, ny

    answer = [x, y]

    return answer