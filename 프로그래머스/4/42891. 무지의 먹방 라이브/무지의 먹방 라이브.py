import heapq

def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    now = 0
    num_foods = len(q)
    while q:
        t, idx = heapq.heappop(q)
        if k < (t - now) * (num_foods):
            heapq.heappush(q, (t, idx))
            break
            
        k -= (t - now) * num_foods
        now = t
        num_foods -= 1
      
    if not q:
        return -1
    
    q.sort(key=lambda x:x[1])
    return q[k % num_foods][1]