import sys
string = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()
boom_last = boom[-1]
boom_len = len(boom)
stack = []

for s in string:
    stack.append(s)
    if s in boom and boom == "".join(stack[-boom_len:]):
        del(stack[-boom_len:])

if stack == []: print("FRULA")
else: print("".join(stack))