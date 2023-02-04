def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = map(int,today.split("."))
    today_day = (today_y * 12*28) + (today_m *28) + today_d
    
    new_term = {}
    
    for idx, term in enumerate(terms):
        type, month = term.split()
        new_term[type] = int(month) * 28
    
    for idx, privacy in enumerate(privacies):
        collect_at, type = privacy.split()
        collect_y, collect_m, collect_d = map(int, collect_at.split("."))
        collect_day = (collect_y * 12*28) + (collect_m *28) + collect_d
        if (today_day - collect_day) >= new_term[type]:
            answer.append(idx+1)
            
    return answer