from itertools import combinations

N, M = map(int, input().split())
houses = []
chickens = []
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 1:
            houses.append((i, j))
        if row[j] == 2:
            chickens.append((i, j))

ans = 1e9
for comb in combinations(chickens, M):
    temp = 0
    for h_i, h_j in houses:
        min_dist = 1e9
        for c_i, c_j in comb:
            min_dist = min(min_dist, abs(c_i-h_i)+abs(c_j-h_j))
        temp += min_dist # 치킨 거리
    ans = min(ans, temp)

print(ans)