def solution(s):
    text_mod = s.replace("{","[").replace("}","]")
    new_list = []
    tmp = []
    string = ''
    cnt =0
    for t in text_mod:
        if cnt >= 1 :
            if t != ',' and t != "]" and t != "[":
                string += t
            elif t == ',':
                tmp.append(int(string))
                string = ''
        if t == "]":
            if string != '':
                tmp.append(int(string))
                string = ''
            if tmp == []:
                continue
            new_list.append(tmp)
            cnt = 0
            tmp = []
        if t == "[":
            cnt +=1 
    new_list.sort(key = lambda x : len(x))
    answer = []  
    for new in new_list:
        for j in new:
            if j not in answer:
                answer.append(j)
        
    return answer

print(solution("{{20,111},{111}}"))