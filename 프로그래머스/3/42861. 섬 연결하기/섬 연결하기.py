def find_parents(x):
    global parents
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union_parents(a, b):
    global parents
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

def solution(n, costs):
    global parents
    parents = [i for i in range(n)]
    
    costs.sort(key=lambda x: x[2])
    
    answer = 0
    for a, b, cost in costs:
        a = find_parents(a)
        b = find_parents(b)
        if a != b:
            union_parents(a, b)
            answer += cost
        
    return answer