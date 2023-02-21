from collections import deque
def solution(maps):
    answer = 0
    start, end, lever = [0,0], [0,0], [0,0]
    n, m = len(maps), len(maps[0])
    
    for idx, map in enumerate(maps): 
        maps[idx] = list(map)
        if 'S' in maps[idx]:
            start = [idx, maps[idx].index('S')]
        if 'E' in maps[idx]:
            end = [idx, maps[idx].index('E')]
        if 'L' in maps[idx]:
            lever = [idx, maps[idx].index('L')]

    def bfs(x,y,target):
        moves = [[-1,0], [1,0],[0,-1],[0,1]]
        visited = [[0] * m for _ in range(n)]
        q = deque()
        q.append((x,y))

        while q:    
            x, y = q.popleft()
            if x== target[0] and y == target[1]:
                return visited[x][y]
            for move in moves:
                nx, ny = x+move[0], y+move[1]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and maps[nx][ny] != "X": #n,m 범위설정 헷갈리지 말기!
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1
        return 0
        
    lever_cnt = bfs(start[0], start[1], lever)
    if lever_cnt == 0: return -1

    end_cnt = bfs(lever[0], lever[1], end)
    if end_cnt == 0 : return -1

    return end_cnt + lever_cnt

print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
# print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))