import sys

input = sys.stdin.readline

n, m = list(map(int, input().strip().split()))
y, x, d = list(map(int, input().strip().split()))
room = [list(map(int, input().strip().split())) for x in range(n)]

def robot_cleaner(n, m, x, y, d, room):
    direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    cnt = 0

    while True:
        if room[y][x] == 0:
            cnt += 1
            room[y][x] = 2

        is_dirty = False
        for i in range(1, 5):
            nd = (d - i) % 4
            nx = x + direction[nd][0]
            ny = y + direction[nd][1]

            if (nx < 0) or (ny < 0) or (nx >= m) or (ny >= n):
                continue

            if room[ny][nx] == 0:
                x, y, d = nx, ny, nd
                is_dirty = True
                break;

        if is_dirty:
            continue

        nx = x - direction[d][0]
        ny = y - direction[d][1]

        if (room[ny][nx] == 1) or (nx < 0) or (ny < 0) or (nx >= m) or (ny >= n):
            return cnt
        else:
            x, y = nx, ny

print(robot_cleaner(n, m, x, y, d, room))