# 틀린 풀이
def solution(n, build_frame):
    answer = []
    # x,y, 구조물 종류(0은 기둥), 설치여부(0은 삭제)
    for x,y,a,b in build_frame:
        if b == 1:
            if a == 0: # 기둥 : 바닥위, 보 한쪽 끝 위, 또 다른 기둥 위
                if y == 0 or [x-1,y,1] in answer or [x,y-1,0] in answer:
                    answer.append([x,y,a])
            else: # 보 : 한쪽 끝 부분이 기둥 위, 양 쪽 끝이 다른 보와 연결
                if [x,y-1,0] in answer or  [x+1,y-1,0] in answer or([x-1,y,1] in answer and [x+1,y,1] in answer):
                    answer.append([x,y,a])

        else:# 이미 세워놓은거 삭제하려한다면
            if a == 0: # 기둥
                remove = True
                if [x,y+1,0] not in answer: # 위에 기둥 없고
                    if [x-1,y+1,1] in answer: # 왼쪽 보 있을 때 
                        if ([x-2,y+1,1] in answer and [x,y+1,1] in answer) or [x-1,y,0] in answer : # 양옆에 보 있거나, 한쪽에 기둥 존재
                            remove = True
                        else: 
                            remove = False
                            continue
                    if [x,y+1,1] in answer:
                        if [x-1,y+1,1] in answer and [x+1,y+1,1] in answer:
                            answer.remove([x,y,a])
                            
    answer.sort()
    return answer 
