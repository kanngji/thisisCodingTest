class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        # 시계 방향
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def dfs(grid,i,j):
            nonlocal max_count
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            count = 1
            
            for d in direction:
                ny = i+d[0]
                nx = j+d[1]
                if nx < 0 or ny < 0 or nx>= len(grid[0]) or ny >= len(grid):
                    continue
                if grid[ny][nx] == 1:
                    count+=dfs(grid,ny,nx)

            if count >= max_count:
                max_count = count
            
            return count


        
        # 세로 i , 가로 j
        for i in range(len(grid)):
            count = 0
            for j in range(len(grid[0])):
                if grid[i][j] ==1:
                    
                    dfs(grid,i,j)
        return max_count
    
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        
        visited = set()
        max_area = 0

        def add_to_queue(queue,i,j):
            if i< 0 or i>= len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] == 0 or (i,j) in visited:
                return
            queue.append((i,j))
            visited.add((i,j))

        def bfs(i,j):
            area = 0
            queue = deque()
            add_to_queue(queue, i ,j)
            while queue:
                for i in range(len(queue)):
                    i,j = queue.popleft()
                    area += 1
                    add_to_queue(queue, i+1,j)
                    add_to_queue(queue, i-1,j)
                    add_to_queue(queue,i,j+1)
                    add_to_queue(queue,i,j-1)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    max_area = max(max_area, bfs(i,j))

        return max_area
