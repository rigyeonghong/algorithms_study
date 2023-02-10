import math
def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    cars = {}
    stack = {}
    for record in records:
        time, num, inout = record.split()
        time = int(time[:2]) * 60 + int(time[3:])
        
        if inout == 'IN':
            cars[num] = time
        elif inout == 'OUT':
            try:
                stack[num] += time - cars[num]
            except:
                stack[num] = time - cars[num]
            del cars[num] 
        
    for car, minute in cars.items():
        try:
            stack[car] += 23*60+59 - minute
        except:
            stack[car] = 23*60+59 - minute
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key = lambda x : x[0])]