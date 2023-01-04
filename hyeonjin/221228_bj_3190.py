import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

apple_loc = []
for i in range(k):
    apple_loc.append(list((map(int, input().strip().split()))))

l = int(input())

rotate_order = deque()
for i in range(l):
    rotate_order.append(input().strip().split())


def snake(n, k, l, apple_loc, rotate_order):
    cnt = 1

    head = [1, 1]
    body = deque()
    direction = deque(["R", "D", "L", "U"])

    while True:
        body.append(head[:])
        if direction[0] == "R":
            head[1] += 1
        elif direction[0] == "D":
            head[0] += 1
        elif direction[0] == "L":
            head[1] -= 1
        elif direction[0] == "U":
            head[0] -= 1

        if head not in body and 0 < head[0] < n + 1 and 0 < head[1] < n + 1:
            if head in apple_loc:
                apple_loc.remove(head)
            else:
                body.popleft()
        else:
            return cnt

        if list(rotate_order) and int(rotate_order[0][0]) == cnt:
            order = rotate_order.popleft()

            if order[1] == "D":
                direction.rotate(-1)
            elif order[1] == "L":
                direction.rotate()

        cnt += 1


print(snake(n, k, l, apple_loc, rotate_order))
