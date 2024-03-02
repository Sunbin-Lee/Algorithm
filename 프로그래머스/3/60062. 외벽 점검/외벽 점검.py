from itertools import permutations

def solution(n, weak, dist):
    num_weak = len(weak)
    weak += [w+n for w in weak]
    
    answer = len(dist) + 1

    for start in range(num_weak):
        for perm in permutations(dist, len(dist)):
            count = 1 # 친구 투입
            pos = weak[start] + perm[count-1] # 해당 친구가 점검할 수 있는 범위
            
            for i in range(start, start+num_weak):
                if pos < weak[i]: # 현재 투입된 친구가 점검할 수 없으면
                    count += 1 # 다음 친구 투입
                    if count > len(dist):
                        break
                    pos = weak[i] + perm[count-1] # 해당 친구가 점검할 수 있는 범위
        
            answer = min(answer, count)
    
    if answer > len(dist): # 불가능한 경우
        return -1
    
    return answer