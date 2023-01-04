import sys

input = sys.stdin.readline

n = input().strip()


def base(n):
    if n[0] == "0":
        if n[1] == "x":
            return int(n[2:], 16)

        return int(n[1:], 8)

    return n


print(base(n))
