# 백준 15684번 사다리 조작
# https://www.acmicpc.net/problem/15684
# Run Time : 0.000
#

import sys
input = sys.stdin.readline

def check():
    for i in range(1, n + 1):
        x = i
        for j in range(1, h + 1):
            if ladder[j][x] == 1:
                x += 1
            elif ladder[j][x - 1] == 1:
                x -= 1
        if x != i:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if cnt >= ans:
        return
    if check():
        ans = cnt
        return
    for i in range(x, h + 1):
        k = y if i == x else 1
        for j in range(k, n):
            if ladder[i][j] == 0 and ladder[i][j - 1] == 0 and ladder[i][j + 1] == 0:
                ladder[i][j] = 1
                dfs(cnt + 1, i, j + 2)
                ladder[i][j] = 0

n, m, h = map(int, input().split())
ladder = [[0] * (n + 1) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a][b] = 1

ans = 4
dfs(0, 1, 1)
print(ans if ans < 4 else -1)