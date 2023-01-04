# 주사위 굴리기
n, m, x, y, k = map(int, input().split())
coo = [[0 for i in range(m)] for j in range(n)]
order = []
for i in range(n):
    coo[i] = list(map(int, input().split()))

order = list(map(int, input().split()))


dice = [0, 0, 0, 0, 0, 0] # 위, 뒤, 오른쪽, 왼쪽, 앞, 아래
def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
    elif dir == 4: #남
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

# 동, 서, 북, 남
dx = [0, 0, -1, 1] 
dy = [1, -1, 0, 0]

nx, ny = x, y
for i in order:
    nx += dx[i-1]
    ny += dy[i-1]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if coo[nx][ny] == 0:
        coo[nx][ny] = dice[5]
    else:
        dice[5] = coo[nx][ny]
        coo[nx][ny] = 0

    print(dice[0])



