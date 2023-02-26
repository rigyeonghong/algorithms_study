def rotate(table):
    return list(map(list,zip(*table[::-1])))

# 퍼즐 한 조각 찾아서, 퍼즐 조각의 실제 위치와 0,0을 기준으로 한 위치와 visited 반환
def dfs(condition,table,key,value,visited):
    x, y, i, j, target = condition
    visited[x][y] = 1
    key.append((x,y)) # 퍼즐 조각의 실제 위치 저장
    value.append((i,j)) # 퍼즐 조각의 0,0을 기준으로 한 위치 저장
    moves = [(-1,0),(1,0),(0,1),(0,-1)] # U D R L
    for move in moves:
        nx, ny = x + move[0], y + move[1]
        if nx < 0 or ny < 0 or nx >= len(table) or ny >= len(table): # 행, 열 길이 같음
            continue
        elif table[nx][ny] == target and visited[nx][ny] == 0:
            key, value, visited = dfs([nx, ny, i+move[0], j+move[1], target], table, key, value, visited)
    return key, value, visited

# 퍼즐 피스들 찾기
def puzzle(table, target):
    visited = [[0]*len(table) for _ in range(len(table))]
    pieces = {} if target == 1 else [] # 테이블의 경우 딕셔너리, 게임보드의 경우 리스트 
    for i in range(len(table)):
        for j in range(len(table)):
            if table[i][j] == target and visited[i][j] == 0:
                key, value , v = dfs([i,j,0,0,target],table,[],[],visited)
                if target == 1: # 테이블인 경우
                    pieces[tuple(key)] = value
                else: # 게임보드인 경우
                    pieces.append(value) # 퍼즐 위치를 0,0을 기준으로 저장한 것을 리스트에 추가
                visited = v # visited를 업데이트
    return pieces

def solution(game_board, table):
    answer = 0
    board = puzzle(game_board, 0) # 게임 보드의 비어있는 퍼즐 조각들 찾기
    for _ in range(4): # 테이블을 4번 회전
        table = rotate(table) # 테이블 회전
        pieces = puzzle(table, 1) # 테이블의 퍼즐 조각들 찾기
        for key, value in pieces.items(): # 테이블의 퍼즐 조각들을 하나씩 확인
            if value in board: # 게임 보드의 비어있는 퍼즐 조각들 중에 해당 퍼즐 조각이 있으면
                board.remove(value)
                answer += len(value)
                for k in key:
                    i, j = k
                    table[i][j] = 0
    return answer