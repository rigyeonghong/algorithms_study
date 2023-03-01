def rotate(table):
    return list(map(list, zip(*table[::-1])))

def is_correct_key(key, M, lock2, N, x, y):
    # 확인용 lock3
    lock3 = [[0 for y in range(N*3)] for x in range(N*3)]
    for i in range(N, N+N):
        for j in range(N, N+N):
            lock3[i][j] = lock2[i][j]
            
    for i in range(x, x+M):
        for j in range(y, y+M):
            lock3[i][j] += key[i-x][j-y]
    
    for i in range(N, N+N):
        for j in range(N, N+N):
            if lock3[i][j] != 1:
                return False
    return True
    

def solution(key, lock):
    M, N = len(key), len(lock)
    # 기존 lock보다 x,y축 모두 3배로 펼친 새로운 lock 생성
    lock2 = [[0 for y in range(N*3)] for x in range(N*3)]
    for x in range(N, N+N):
        for y in range(N, N+N):
            lock2[x][y] = lock[x-N][y-N]

    for _ in range(4):
        key = rotate(key)
        
        # key가 새로운 lock에 들어갈 x,y값 범위
        for x in range(N-M+1, N+N):
            for y in range(N-M+1, N+N):
                is_correct = is_correct_key(key, M, lock2, N, x, y)
                
                if is_correct == True: return True
                
    return False