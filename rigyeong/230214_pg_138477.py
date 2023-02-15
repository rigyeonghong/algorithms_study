def solution(k, score):
    answer = []
    award = []
    for s in score:
        award.append(s)
        award.sort(reverse=True)
        if len(award) < k: answer.append(award[-1])
        else: answer.append(award[k-1])
    return answer

# ref : 시간은 비슷
import heapq
def solution(k, score):
    answer = []
    award = []

    for s in score:
        heapq.heappush(award, -s)
        answer.append(max(heapq.nsmallest(k, award))*(-1))

    return answer