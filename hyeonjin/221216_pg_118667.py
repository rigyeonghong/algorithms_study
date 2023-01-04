from collections import deque


def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_1 = sum(q1)
    sum_2 = sum(q2)

    cnt = 0
    while cnt <= len(queue1 + queue2) * 2:
        if sum_1 == sum_2:
            return cnt

        cnt += 1

        if sum_1 > sum_2:
            pop = q1.popleft()
            q2.append(pop)

            sum_1 -= pop
            sum_2 += pop

        elif sum_1 < sum_2:
            pop = q2.popleft()
            q1.append(pop)

            sum_1 += pop
            sum_2 -= pop

    return -1
