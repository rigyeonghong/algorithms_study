from collections import defaultdict
def solution(weights):
    cnt = 0
    pos = [(2,3), (2,4), (3,4), (4,3), (2,1), (3,2)]
    
    weight_map = defaultdict(int)
    for w in weights:
        weight_map[w] += 1

    for my_w in weight_map: # pos로 for문을 돌면 weight로 도는거에 비해 훨씬 덜 돌게됨
        if weight_map[my_w] > 1:
            cnt += weight_map[my_w] *(weight_map[my_w]-1) //2 # 중복 허용 (조합)
        for (my_pos, friend_pos) in pos:
            expected_w = my_w * my_pos / friend_pos
            if (expected_w in weight_map): 
                cnt += weight_map[my_w] * weight_map[expected_w]
        weight_map[my_w] = 0 
        
    return cnt