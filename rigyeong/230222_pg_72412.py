# 효율성 통과 못함
def solution(info, query):
    answer =[]
    language={'cpp':[], 'java':[], 'python':[]}
    job={'backend':[], 'frontend':[]}
    career={'junior':[], 'senior':[]}
    food ={'chicken':[], 'pizza':[]}
    score =[]
    p = [] 
    
    for idx, val in enumerate(info):
        a,b,c,d,e = val.split()
        language[a].append(idx)
        job[b].append(idx)
        career[c].append(idx)
        food[d].append(idx)
        score.append([int(e),idx])
        p.append(idx) 
        
    score.sort()
        
    for q in query:
        want = q.split(' ')
        a,b,c,d,e = want[0], want[2], want[4], want[6], int(want[7])
        flag_a, flag_b, flag_c,flag_d = False,False,False,False
        
        if a != '-': select_a = language[a]
        else: select_a = p
            
        if b != '-': select_b = job[b]
        else: select_b = p
            
        if c != '-': select_c = career[c]
        else: select_c = p
            
        if d != '-': select_d = food[d]
        else: select_d = p
            
        
        select_e =[]
        for s, people in score:
            if s >= e:
                select_e.append(people)
                
        result = list(set(select_a) & set(select_b) & set(select_c) & set(select_d) & set(select_e)) 
        answer.append(len(result))
    
    return answer