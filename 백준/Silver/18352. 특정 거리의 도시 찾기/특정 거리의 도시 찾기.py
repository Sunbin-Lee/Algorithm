from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((X, 0))

visited = [0 for _ in range(N+1)]

answer = []
while q:
    now, dist = q.popleft()
    visited[now] = 1

    if dist == K:
        answer.append(now)
    elif dist > K:
        break

    for node in graph[now]:
        if visited[node] == 1:
            continue

        q.append((node, dist + 1))
        visited[node] = 1

# print(answer)
if not answer:
    print(-1)
else:
    answer.sort()
    for node in answer:
        print(node)