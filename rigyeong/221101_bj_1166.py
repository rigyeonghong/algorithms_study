import sys
n, l, w, h = map(int, sys.stdin.readline().split())
start, end = 0, max(l, w, h)

for _ in range(10000):
    mid = (start + end) / 2
    count = (l // mid) * (w // mid) * (h // mid)
    if count >= n:
        start = mid
    else:
        end = mid

print("%.10f" %(end))