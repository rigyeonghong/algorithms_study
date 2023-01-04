import sys

input = sys.stdin.readline

n, m, y, x, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
orders = list(map(int, input().split()))

dice = [0] * 6
move = [[1, 0], [-1, 0], [0, -1], [0, 1]]

dice_change = [
    [4, 2, 1, 6, 5, 3],
    [3, 2, 6, 1, 5, 4],
    [5, 1, 3, 4, 6, 2],
    [2, 6, 3, 4, 1, 5],
]


def chage_dice(dice, order):
    temp_dice = [o for o in dice]

    for i in range(6):
        dice[i] = temp_dice[dice_change[order][i] - 1]


for order in orders:
    order -= 1

    next_x = x + move[order][0]
    next_y = y + move[order][1]
    if (next_x >= m) or (0 > next_x) or (next_y >= n) or (0 > next_y):
        continue

    x = next_x
    y = next_y

    chage_dice(dice, order)

    if board[y][x] == 0:
        board[y][x] = dice[5]
    else:
        dice[5] = board[y][x]
        board[y][x] = 0

    print(dice[0])
