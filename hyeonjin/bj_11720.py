import sys

input = sys.stdin.readline

n = int(input())
nums = input().strip()

print(sum(map(int, list(nums))))
