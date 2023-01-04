import sys
from collections import deque
n,m = map(int, sys.stdin.readline().split())
graph = []
r,c,d = map(int, sys.stdin.readline().split())
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

# d => 0,3,2,1 순서로 돌아야함.
dx = [-1,0,1,0]
dy = [0,1,0,-1]

cnt = 1
graph[r][c] = 2

while 1:
    flag = 0
    for _ in range(4): # 4방향 확인
        nx = r + dx[(d+3) %4]
        ny = c + dy[(d+3) %4]
        # 한번 돌았으면 그 방향으로 작업시작
        d = (d+3) % 4
        if graph[nx][ny] == 0 :
            graph[nx][ny] = 2
            cnt += 1
            r = nx
            c = ny
            # 청소 한 방향이라도 했으면 다음으로 넘어감
            flag = 1
            break
    
    if flag == 0: # 4방향 모두 청소 되어 있을 때,
        if graph[r-dx[d]][c-dy[d]] == 1: # 후진했는데 벽
            print(cnt)
            break
        else:
            r, c = r-dx[d], c-dy[d]