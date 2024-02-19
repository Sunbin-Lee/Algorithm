def find_parents(parents, x):
    if parents[x] != x:
        parents[x] = find_parents(parents, parents[x])
    return parents[x]

def union_parents(parents, a, b):
    a = find_parents(parents, a)
    b = find_parents(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

N = int(input())
xs = []
ys = []
zs = []
for i in range(N):
    x, y, z = map(int, input().split())
    xs.append((x, i+1))
    ys.append((y, i+1))
    zs.append((z, i+1))

xs.sort()
ys.sort()
zs.sort()

edges = []
for i in range(N-1):
    edges.append((xs[i+1][0] - xs[i][0], xs[i+1][1], xs[i][1]))
    edges.append((ys[i+1][0] - ys[i][0], ys[i+1][1], ys[i][1]))
    edges.append((zs[i+1][0] - zs[i][0], zs[i+1][1], zs[i][1]))

edges.sort()

ans = 0
parents = [i for i in range(N+1)]
for edge in edges:
    dist, i, j = edge
    p_i = find_parents(parents, i)
    p_j = find_parents(parents, j)
    if p_i != p_j: # cycle
        union_parents(parents, p_i, p_j)
        ans += dist

print(ans)