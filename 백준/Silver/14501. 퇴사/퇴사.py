N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0 for _ in range(N)] # 해당 날짜의 상담을 했을 때 얻을 수 있는 최대 이익
for i in range(N):
    if i + arr[i][0] > N:
        continue
    profit = 0
    for j in range(i):
        if i >= j + arr[j][0]:
            profit = max(profit, dp[j])
    dp[i] = profit + arr[i][1]

print(max(dp))