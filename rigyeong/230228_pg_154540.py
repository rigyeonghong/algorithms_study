from collections import deque
def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[1])
    visited = [[0]*m for _ in range(n)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    def dfs(x,y,visited):
        q = deque()
        q.append([x,y])
        cnt = 0
        
        while q:
            x , y = q.popleft()
            if maps[x][y] != "X":
                cnt += int(maps[x][y])
            visited[x][y] = 1
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < n and 0<= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != "X" and [nx, ny] not in q:
                    q.append([nx,ny])
        answer.append(cnt)
        return
    
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and maps[i][j] != "X":
                dfs(i,j,visited)
    if answer == []: return [-1]
    else : return sorted(answer)