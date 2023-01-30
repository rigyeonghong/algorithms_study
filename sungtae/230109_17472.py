# 백준 다리만들기2 17472
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
land = dict()
land_arr = []

# 섬 구분하여 좌표 구하기
land_num = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            queue = deque([(i,j)])
            visited[i][j] = True
            land[(i,j)] = land_num
            land_arr.append((i, j, land_num))   # 다리 만드는 데에 사용하기 위함
            while queue:
                y, x = queue.popleft()
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0<=ny<n and 0<=nx<m and not visited[ny][nx] and board[ny][nx]:
                        queue.append((ny, nx))
                        visited[ny][nx] = True
                        land[(ny, nx)] = land_num
                        land_arr.append((ny, nx, land_num))
            land_num += 1

# 다리 제작
edges = []
for y, x, curr_land in land_arr:
    for k in range(4):
        dist = 0
        ny = y + dy[k]
        nx = x + dx[k]
        while True:
            if 0<=ny<n and 0<=nx<m:
                to_land = land.get((ny, nx))
                # 같은 섬인 경우
                if curr_land == to_land:
                    break
                # 바다 위, 다리길이 +1
                if to_land == None:
                    ny += dy[k]
                    nx += dx[k]
                    dist += 1
                    continue
                # 다리가 짧음
                if dist < 2:
                    break
                edges.append((dist, curr_land, to_land))
                break
            else:
                break
edges = sorted(edges, reverse=True)

# 크루스칼 알고리즘
def union(y, x):
    y = find(y)
    x = find(x)
    parents[x] = y

def find(k):
    if k != parents[k]:
        parents[k] = find(parents[k])
    return parents[k]

ans = 0
cnt = land_num-1
parents = [i for i in range(land_num)]
while cnt:
    try:
        w,a,b = edges.pop()
    except:
        # empty list, 다리 부족
        print(-1)
        sys.exit()
    if find(a) != find(b):
        union(a, b)
        ans += w
        cnt -= 1

print(ans)


