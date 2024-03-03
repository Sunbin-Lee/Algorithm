from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [1e9 for _ in range(N+1)]
dist[X] = 0
q = deque([X])
while q:
    now = q.popleft()
    for node in graph[now]:
        if dist[node] != 1e9:
            continue
        dist[node] = dist[now] + 1
        q.append(node)

ans = False
for n in range(1, N+1):
    if dist[n] == K:
        print(n)
        ans = True

if not ans:
    print(-1)