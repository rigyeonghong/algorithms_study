import sys
from collections import deque
n,l,r = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
is_move = 0

def bfs(x, y, visited, graph):
    global is_move
    people = graph[x][y]
    cnt = 1
    q = deque()
    q.append([x,y])
    visited[x][y] = 1

    temp = []
    temp.append([x,y])

    while q:
        pop_x, pop_y = q.popleft()

        for i in range(4):
            nx, ny = pop_x + dx[i], pop_y + dy[i]
            if 0<= nx <n and 0<= ny <n and visited[nx][ny] == 0:
                if l<=abs(graph[pop_x][pop_y]-graph[nx][ny])<=r:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    people += graph[nx][ny]
                    cnt +=1 
                    temp.append([nx,ny]) 

    move_people = people // cnt

    if cnt > 1:
        is_move = 1
        for x,y in temp:
            graph[x][y] = move_people

answer= 0
while True:
    visited = [[0] * n for i in range(n)]
    is_move = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i,j,visited, graph)

    if is_move == 0:
        break
    answer += 1
print(answer)