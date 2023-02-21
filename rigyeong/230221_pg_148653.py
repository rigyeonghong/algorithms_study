def solution(storey):
    answer = 0
    storey_list = list(map(int, list(str(storey))))[::-1]
    storey_list.append(0)
    for idx, s in enumerate(storey_list):
        if s >= 10:
            if idx == len(storey_list) -1: # 더이상 뒷자리가 없을 때
                answer += s//10
                s = s% 10
            else:
                storey_list[idx+1] += s//10
                s = s% 10
        
        if s < 5:
            answer += s
        elif s > 5:
            answer += 10 - s
            if idx == len(storey_list) -1:
                answer += 1
            else:
                storey_list[idx+1] += 1
        else:
            if 5 <= storey_list[idx+1] <= 9:
                answer += 10 - s
                if idx == len(storey_list) -1:
                    answer += 1
                else:
                    storey_list[idx+1] += 1
            else:
                answer += s
    return answer