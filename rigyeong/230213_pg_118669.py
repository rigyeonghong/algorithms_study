from heapq import heappop, heappush

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    summits.sort() 
    summits_set = set(summits) # 시간초과 방지..
    for i, j, w  in paths:
        graph[i].append((w,j))
        graph[j].append((w,i))

    com = [] # (intensity, node)
    visited = [10000001] * (n + 1)
    for gate in gates:
        heappush(com, (0,gate))
        visited[gate] = 0
    
    while com:
        intensity, node = heappop(com)
        
        if node in summits_set or intensity > visited[node]:
            continue
            
        for w, next_node in graph[node]:
            new_intensity = max(intensity, w)
            if new_intensity < visited[next_node]:
                visited[next_node] = new_intensity
                heappush(com, (new_intensity, next_node))
                
    answer = [0, 10000001]
    for summit in summits:
        if visited[summit] < answer[1]:
            answer[0] = summit
            answer[1] = visited[summit]
    
    return answer