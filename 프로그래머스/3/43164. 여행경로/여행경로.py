def dfs(now, route, tickets, used):
    global answer
    if len(route) == len(tickets) + 1:
        answer.append(route)
        return
        
    for i in range(len(tickets)):
        if used[i] == 0 and tickets[i][0] == now:
            used[i] = 1
            dfs(tickets[i][1], route+[tickets[i][1]], tickets, used)
            used[i] = 0
    
def solution(tickets):
    global answer
    answer = []
    
    used = [0 for _ in range(len(tickets))]
    dfs('ICN', ['ICN'], tickets, used)
        
    return min(answer)