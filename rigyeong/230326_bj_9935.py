import sys
string = sys.stdin.readline().strip()
boom = sys.stdin.readline().strip()

lastChar = boom[-1] 
length = len(boom)
stack = []

for s in string:
    stack.append(s)
    if s == lastChar and ''.join(stack[-length:]) == boom:
        del stack[-length:]

ans = ''.join(stack)

if ans == '': print("FRULA")
else: print(ans)