from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def bfs(i, j):
    q = deque([(i, j)])
    union_q = deque( [(i, j)])
    visited[i][j] = True
    total = arr[i][j]
    cnt = 1

    while q:
        x, y = q.popleft()

        for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                    q.append((nx, ny))
                    union_q.append((nx, ny))
                    visited[nx][ny] = True
                    total += arr[nx][ny]
                    cnt += 1

    return cnt, total, union_q

ans = 0
while True:
    visited = [[False] * n for _ in range(n)]
    flag = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                cnt, total, union_q = bfs(i, j)
                if cnt > 1:
                    flag = True
                    for x, y in union_q:
                        arr[x][y] = total // cnt
    if not flag:
        break
    ans += 1
    
print(ans)

