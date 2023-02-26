from itertools import combinations
def solution(orders, course):
    answer = []

    for c in course:
        dict = {}
        combi =[]
        for order in orders:
            combi.extend(list(combinations(sorted(order), c))) 
        
        for com in combi:
            order_str = ''.join(com)
            if order_str in dict:
                dict[order_str] += 1
            else:
                dict[order_str] = 1
    
        max_dict = 0
        for d in dict: max_dict= max(max_dict, dict[d] )
        for d in dict:
            if dict[d] == max_dict:
                if dict[d] > 1:
                    answer.append(d)

    return sorted(answer)