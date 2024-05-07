class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direct =[(0,1),(1,0),(-1,0),(0,-1)]
        def dfs(grid,i,j):
            if grid[i][j] == 0:
                return
            grid[i][j] = 0

            for d in direct:
                ny = i+d[0]
                nx = j+d[1]
                if nx < 0 or ny < 0 or nx>= len(grid[0]) or ny >= len(grid):
                    continue
                if grid[ny][nx] == '1':
                    dfs(grid,ny,nx)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count+=1
                    dfs(grid,i,j)
        return count

# def 함수 위치
# bfs
    
# if not grid:
#     return 0

# direct = [(1,0),(-1,0),(0,1),(0,-1)]
# cnt = 0

# for i in range(len(grid)): #세로
#     for j in range(len(grid[0])): #가로
#         if grid[i][j] == '1':
#             cnt+=1
#             queue = deque([(i,j)])
#             while queue:
#                 y,x = queue.popleft()
#                 if 0<=y <len(grid) and 0<=x<len(grid[0]) and grid[y][x]:
#                     grid[y][x] = '0'
#                     for dy , dx in direct:
#                         queue.append((y+dy),(x+dx))
# return cnt                  