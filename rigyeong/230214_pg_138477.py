def solution(k, score):
    answer = []
    award = []
    for s in score:
        award.append(s)
        award.sort(reverse=True)
        if len(award) < k: answer.append(award[-1])
        else: answer.append(award[k-1])
    return answer