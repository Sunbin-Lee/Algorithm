from bisect import bisect_left, bisect_right

def count_values(lst, q):
    q_lower = q.replace('?', 'a')
    q_upper = q.replace('?', 'z')
    
    first = bisect_left(lst, q_lower)
    last = bisect_right(lst, q_upper)
    return last - first

def solution(words, queries):
    arr = [[] for _ in range(10001)]
    reverse_arr = [[] for _ in range(10001)]
    
    for w in words:
        arr[len(w)].append(w)
        reverse_arr[len(w)].append(w[::-1])
    
    for i in range(10001):
        arr[i].sort()
        reverse_arr[i].sort()

    answer = []
    for q in queries:
        if q[0] == '?':
            c = count_values(reverse_arr[len(q)], q[::-1])
        else:
            c = count_values(arr[len(q)], q)
        answer.append(c)
    
    return answer