# ref : 걸리는 시간의 최솟값. BFS
import sys
from collections import deque
n = int(sys.stdin.readline())
tmp = [[-1] *(n+1) for _ in range(n+1)]
q = deque((1,0)) # 화면 이모티콘 개수, 클립보드 이모티콘 개수
tmp[1][0] = 0
while q:
    s, c = q.popleft()
    if tmp[s][s] == -1: # 방문하지 않았으면
        # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
        tmp[s][s] = tmp[s][c] + 1 
        q.append((s,s))
    if s+c <= n and tmp[s+c][c] == -1:
        # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기  : (s+c,c) <- (s,s)
        tmp[s+c][c] = tmp[s][c] + 1 
        q.append((s+c, c))
    if s-1 >= 0 and tmp[s-1][c] == -1:
        # 화면에 있는 이모티콘 중 하나를 삭제 : (s-1, c) <- (s,s)
        tmp[s-1][c] = tmp[s][c] + 1 
        q.append((s-1, c))
answer = -1
for i in range(n+1):
    if tmp[n][i] != -1:
        if answer == -1 or answer > tmp[n][i]:
            answer = tmp[n][i]
print(answer)