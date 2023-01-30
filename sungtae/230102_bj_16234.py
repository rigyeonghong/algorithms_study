# 인구 이동
# pypy로 돌아감
import sys
sys.setrecursionlimit(5000)
n, l, r = map(int, input().split())
land = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    land[i] = list(map(int, input().split()))

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

def dfs(y, x, visited, unite):
    visited.append((y, x))
    unite.append((y, x))
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < n and 0 <= nx < n:
        
            if (ny, nx) not in visited:
                if l <= abs(land[y][x] - land[ny][nx]) <= r:
                    dfs(ny, nx, visited, unite)
    return unite


cnt = 0
while(1):
    visited = []
    flag = 0
    unite = []
    for i in range(n):
        for j in range(n):
            # for k in range(4):
            #     ny = i + dy[k]
            #     nx = j + dx[k]
            #     if 0 <= ny < n and 0 <= nx < n:
            if (i, j) not in visited:
                if l <= abs(land[i][j] - land[ny][nx]) <= r:
                    unite = []
                    unite = dfs(i, j, visited, unite)
            
                    sum = 0
                    for elem in unite:
                        sum += land[elem[0]][elem[1]]
                    sum = sum // len(unite)
                    for elem in unite:
                        land[elem[0]][elem[1]] = sum    
                    flag = 1 
    if (flag == 0):
        break
    cnt += 1
print(cnt)
