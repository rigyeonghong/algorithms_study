from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[-1] *20 for _ in range(20)]
    for rec in rectangle:
        x1,y1,x2,y2 = map(lambda x: 2*x, rec)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0: # 테두리가 이전 사각형의 내부면 표시하면 안됨
                    field[i][j] = 1

    moves = [[-1,0],[1,0],[0,-1],[0,1]]
    visited = [[0]*102 for _ in range(102)]
    q = deque()
    q.append([characterX * 2, characterY * 2])
    
    while q:
        x, y = q.popleft()
        
        if x == itemX*2 and y == itemY*2:
            answer = visited[x][y] // 2
            break
        
        for m in moves:
            nx, ny = x + m[0], y + m[1]
            if field[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx,ny])
                visited[nx][ny] = visited[x][y] + 1 
    return answer

print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))