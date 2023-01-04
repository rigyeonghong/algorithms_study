import sys
str1 = list(sys.stdin.readline().strip())
str2 = []

for _ in range(int(sys.stdin.readline())):
    c = list(sys.stdin.readline().split())
    if c[0] == "L":
        if str1:
            str2.append(str1.pop())

    elif c[0] == "D":
        if str2:
            str1.append(str2.pop())

    elif c[0] == "B":
        if str1:
            str1.pop()
    else:
        str1.append(c[1])

str1.extend(reversed(str2))
print("".join(str1))
