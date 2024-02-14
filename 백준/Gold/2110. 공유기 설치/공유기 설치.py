N, C = map(int, input().split())
coords = []
for _ in range(N):
    coords.append(int(input()))
coords.sort()

# 가장 인접한 공유기 사이 거리
ans = 0
s, e = 1, coords[-1] - coords[0]
while s <= e:
    l = (s + e)//2
    i, j = 0, 1
    count = 0
    while j < N:
        if coords[j] - coords[i] >= l:
            count += 1
            i = j
        j += 1

    if count >= C - 1:
        ans = l
        s = l + 1
    else:
        e = l - 1

print(ans)