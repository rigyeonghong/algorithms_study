import sys
n = int(sys.stdin.readline())
m = []
def dfs():
    if len(m) == n:
        print(*m)
        return
    for i in range(1, n + 1):
        if i not in m:
            m.append(i)
            dfs()
            m.pop()
dfs()