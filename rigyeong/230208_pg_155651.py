def solution(book_time):
    cnt = 1
    book_times = []
    for time in book_time:
        start = int(time[0][0:2]) * 60 + int(time[0][3:])
        end = int(time[1][0:2]) * 60 + int(time[1][3:])
        book_times.append([start, end])
    book_times.sort()

    rooms =[]
    for s, e in book_times:
        if rooms == []:
            rooms.append(e+10)
            continue
        rooms.sort()
        if rooms[0] <= s:
            rooms[0] = e+10
        else:
            rooms.append(e+10)
    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
