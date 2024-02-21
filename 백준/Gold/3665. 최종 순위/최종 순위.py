from collections import deque

T = int(input())
for _ in range(T):
    ans = None
    n = int(input())
    teams = list(map(int, input().split()))

    graph = [[0 for _ in range(n+1)] for _ in range(n+1)] # i > j 관계를 나타냄
    indegree = [0 for _ in range(n+1)]
    for i in range(n):
        for j in range(i+1, n):
            graph[teams[i]][teams[j]] = 1
            indegree[teams[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if graph[a][b] == 1: # a > b였다면
            graph[a][b] = 0
            graph[b][a] = 1
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = 0
            graph[a][b] = 1
            indegree[a] -= 1
            indegree[b] += 1

    q = deque([])
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    cycle, unique = False, True
    ans = []
    for _ in range(n):
        if len(q) == 0: # 일관성이 없는 경우
            cycle = True
            break
        if len(q) > 2: # 확실한 순위를 찾을 수 없는 경우
            unique = False
            break

        now = q.popleft()
        ans.append(now)
        for i in range(1, n+1):
            if graph[now][i] == 1:
                graph[now][i] = 0
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print('IMPOSSIBLE')
    elif not unique:
        print('?')
    else:
        print(*ans)