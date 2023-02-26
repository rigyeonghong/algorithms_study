from collections import deque
import copy
def solution(maps):
    n, m = len(maps), len(maps[0])
    
    def bfs(x,y):
        q = deque()
        q.append([x,y])
        check = copy.deepcopy(maps)
        visited = [[0]*m for _ in range(n)]
        visited[x][y] = 1
        
        moves = [[-1,0],[1,0],[0,-1],[0,1]]
        while q:
            x, y = q.popleft()
            for move in moves:
                nx, ny = x+move[0], y+move[1]
                if 0<= nx < n and 0 <= ny < m and check[nx][ny] != 0 and visited[nx][ny] == 0:
                    if check[nx][ny] > 1:
                        check[nx][ny] = min(check[nx][ny], check[x][y] + 1)
                    else:
                        check[nx][ny] = check[x][y] + 1
                    visited[nx][ny] = 1
                    q.append([nx,ny])

        return check[0][0]
    
    result = bfs(n-1,m-1)
    if result == 1: return -1
    else : return result 

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))