def solution(n, m, x, y, r, c, k):
    diff = abs(x-r) + abs(y-c)
    if diff % 2 != k%2 or diff > k:
        return 'impossible'
    stack = [(x,y,[])]
    while stack:
        x_pos, y_pos, path = stack.pop()
        if len(path) == k and (x_pos, y_pos) == (r,c):
            answer = ''.join(path)
            break
        remain, shortest_path = k - len(path), abs(x_pos-r) + abs(y_pos-c)
        if remain < shortest_path or remain % 2 != shortest_path % 2:
            continue            
        if x_pos > 1:
            stack.append((x_pos - 1, y_pos, path + ['u']))
        if y_pos < m:
            stack.append((x_pos, y_pos + 1, path + ['r']))
        if y_pos > 1:
            stack.append((x_pos, y_pos - 1, path + ['l']))
        if x_pos < n:
            stack.append((x_pos + 1, y_pos, path + ['d']))
    return answer

print(solution(3, 3, 1, 2, 3, 3, 4))