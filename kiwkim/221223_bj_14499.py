import sys

N, M, y, x, K = map(int, sys.stdin.readline().split())
Map = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    for j in range(len(numbers)):
        Map[i][j] = numbers[j]

dice = [0 for _ in range(6)]
direction = list(map(int, sys.stdin.readline().split()))
for k in direction:
    flag = False
    if k == 1:
        if x + 1 < M:
            x += 1
            dice[1], dice[2], dice[3], dice[5] = dice[5], dice[1], dice[2], dice[3]
            flag = True
    elif k == 2:
        if x - 1 >= 0:
            x -= 1
            dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
            flag = True
    elif k == 3:
        if y - 1 >= 0:
            y -= 1
            dice[0], dice[2], dice[4], dice[5] = dice[5], dice[0], dice[2], dice[4]
            flag = True
    elif k == 4:
        if y + 1 < N:
            y += 1
            dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
            flag = True
    if flag:
        print(dice[2])
        if Map[y][x] == 0:
            Map[y][x] = dice[5]
        else:
            dice[5] = Map[y][x]
            Map[y][x] = 0

