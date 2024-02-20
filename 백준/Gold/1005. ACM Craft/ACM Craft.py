from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))

    graph = [[] for _ in range(N+1)]
    graph_reverse = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[X].append(Y)
        graph_reverse[Y].append(X)
        indegree[Y] += 1

    W = int(input())

    q = deque([])
    for node in range(1, N+1):
        if indegree[node] == 0:
            q.append(node)

    elapsed_times = [0 for _ in range(N+1)] # 경과시간
    for i in range(1, N+1):
        elapsed_times[i] = times[i]

    while q:
        now = q.popleft()
        for n in graph[now]:
            indegree[n] -= 1
            elapsed_times[n] = max(elapsed_times[n], elapsed_times[now] + times[n])
            if indegree[n] == 0:
                q.append(n)

    print(elapsed_times[W])