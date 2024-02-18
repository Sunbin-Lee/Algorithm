n = int(input())
m = int(input())
arr = [[1e9 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b, cost = map(int, input().split())
    if cost < arr[a-1][b-1]: # 비용이 최소인 노선 반영
        arr[a-1][b-1] = cost

for i in range(n):
    arr[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if arr[i][k] + arr[k][j] < arr[i][j]:
                arr[i][j] = arr[i][k] + arr[k][j]

# 갈 수 없는 경우 처리
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1e9:
            arr[i][j] = 0

for row in arr:
    print(*row)