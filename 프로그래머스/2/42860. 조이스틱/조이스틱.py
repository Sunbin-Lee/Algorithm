def dfs(count, now, move):
    global answer
    if sum(count) == 0:
        answer = min(answer, move)
    
    temp_r = None
    for r in range(len(count)):
        now_r = (now+r)%len(count)
        if count[now_r] > 0:
            count[now_r], temp = 0, count[now_r]
            dfs(count, now_r, move+r+temp)
            count[now_r] = temp
            break

    for l in range(1, len(count)):
        now_l = (now-l+len(count))%len(count)
        if count[now_l] > 0:
            count[now_l], temp = 0, count[now_l]
            dfs(count, now_l, move+l+temp)
            count[now_l] = temp
            break

def solution(name):
    global answer
    answer = int(1e9)
    
    count = [min(ord('Z')-ord(s)+1, ord(s)-ord('A')) for s in name]
    
    dfs(count, 0, 0)
    print(answer)
    
    return answer 