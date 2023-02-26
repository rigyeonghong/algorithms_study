def solution(board):
    num={'O':0,'X':0}
    flag={'O':False,'X':False}
    dir=[(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1),(1,0),(0,1),(1,1)]

    for r in range(3):
        for c in range(3):
            if board[r][c]!='.':
                target=board[r][c] 
                num[target]+=1 # 'O'와 'X' 갯수 세기
                for d in dir:
                    temp=[False,False]
                    for i in range(1,3): # i = 1, 2
                        dx=r+d[0]*i
                        dy=c+d[1]*i
                        if dx<0 or dx>2 or dy<0 or dy>2:
                            break
                        if board[dx][dy]==target:
                            temp[i-1]=True
                    if temp[0] and temp[1]:
                        flag[target]=True 

    if num['X']>num['O'] or num['O']-num['X']>1: # x가 더 많거나, 0이 2이상으로 많다면 
        return 0
    if flag['O'] and flag['X']: # 둘 다 이겼다면 = 이겼는데 더 진행한 것
        return 0
    if flag['O'] and num['O']==num['X']: # 0이 이겼는데 둘의 갯수가 같다면 = 이겼는데 더 진행한 것
        return 0
    if flag['X'] and num['O']>num['X']: # X가 이겼는데, 0의 갯수가 더 많다면 = 이겼는데 더 진행한 것
        return 0
    return 1