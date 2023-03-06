def rotate(table):
    return list(map(list, zip(*table[::-1])))

def is_correct(key, lock, x, y):
    new_lock = [item[:] for item in lock] # 약 4배이상 빨라짐
    
    # 항상 len(key) < len(lock)
    for i in range(x,x+len(key)):
        for j in range(y,y+len(key)):
            if i < 0 or j < 0 or i >= len(lock) or j >= len(lock):
                continue
            else:
                new_lock[i][j] += key[i-x][j-y]
    N = int(len(lock)/3)   

    # O(N^2) = 20 * 20 = 400
    for i in range(N, N+N):
        for j in range(N, N+N):
            if new_lock[i][j] == 0 or new_lock[i][j] > 1:
                return False
    return True

def solution(key, lock):
    answer = False
    M, N = len(key), len(lock)
    new_lock = [[0] *N*3 for _ in range(N*3)]
    for i in range(N-M+1, N+N):
        for j in range(N-M+1, N+N):
            new_lock[i][j] = lock[i-N][j-N]
    
    # O(N^2) = 20 * 20 = 400
    for _ in range(4):
        key = rotate(key)
        for i in range(len(new_lock)):
            for j in range(len(new_lock)):
                if is_correct(key, new_lock, i, j):
                    return True
    
    return answer

# O(N^4) = 20^4 = 160000
print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))