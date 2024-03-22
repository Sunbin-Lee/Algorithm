import heapq

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

distance = [1e9 for _ in range(N+1)]
distance[start] = 0
q = [(0, start)]
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist: # 이미 처리된 노드
        continue
    for node, cost in graph[now]:
        new_cost = dist + cost
        if new_cost < distance[node]:
            distance[node] = new_cost
            heapq.heappush(q, (new_cost, node))

print(distance[end])