def solution(m, n, puddles):
    map_arr = [[0 for _ in range(m)] for _ in range(n)]
    for a, b in puddles:
        map_arr[b-1][a-1] = -1
        
    dp = [[0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        if map_arr[i][0] == -1:
            break
        dp[i][0] = 1
        
    for j in range(m):
        if map_arr[0][j] == -1:
            break
        dp[0][j] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if map_arr[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    answer = dp[n-1][m-1] % 1000000007
    return answer