def solution(money):
    n = len(money)
    
    dp1 = [0 for _ in range(n)] 
    dp1[0] = money[0] # 첫 집을 턴 경우
    for i in range(1, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
    dp1[n-1] = dp1[n-2] # 마지막 집은 털지 않음
        
    dp2 = [0 for _ in range(n)]
    dp2[0] = 0 # 첫 집을 털지 않은 경우
    for i in range(1, n): # 마지막 집을 텀
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    
    ans = max(dp1[n-1], dp2[n-1])
    return ans