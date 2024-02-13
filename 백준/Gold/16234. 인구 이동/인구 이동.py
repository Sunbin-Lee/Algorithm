from collections import deque

steps = [(-1,0), (1,0), (0,-1), (0,1)]

def make_group(arr, visited, i, j):
    group = [(i, j)]
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        i, j = q.popleft()
        for s in steps:
            new_i = i + s[0]
            new_j = j + s[1]
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                continue
            if visited[new_i][new_j] == 1:
                continue

            diff = abs(arr[new_i][new_j] - arr[i][j])
            if L <= diff <= R:
                group.append((new_i, new_j))
                q.append((new_i, new_j))
                visited[new_i][new_j] = 1

    return group

def check(arr):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 1:
                continue

            group = make_group(arr, visited, i, j)
            if len(group) > 1:
                groups.append(group)

    return groups

def move(arr, groups):
    for g in groups:
        sum_p = 0
        for i, j in g:
            sum_p += arr[i][j]
        avg_p = sum_p // len(g)
        for i, j in g:
            arr[i][j] = avg_p

N, L, R = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

ans = 0
while True:
    groups = check(arr)
    if len(groups) < 1:
        break
    move(arr, groups)
    ans += 1

print(ans)
