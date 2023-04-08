
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid[0]), len(grid)
        visited = [[0] *(n) for _ in range(m)]
        
        def bfs(x,y,visited,n,m):
            q = deque()
            q.append([x,y])
            delta = [[0,1],[0,-1],[1,0],[-1,0]]
            visited[x][y] = 1

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + delta[i][0], y + delta[i][1]
                    if 0 <= nx < m and  0 <= ny < n and visited[nx][ny] == 0 and grid[nx][ny] == "1":
                        q.append([nx,ny])
                        visited[nx][ny] = 1
            
            return 
        
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    bfs(i,j,visited,n,m)
                    cnt += 1
        return cnt

