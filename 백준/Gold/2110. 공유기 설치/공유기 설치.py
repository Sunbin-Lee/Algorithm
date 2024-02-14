N, C = map(int, input().split())
h_list = []
for _ in range(N):
    h_list.append(int(input()))
h_list.sort()

# 거리를 search
start = 1
end = h_list[-1]
answer = 0
while start<=end:
    mid = (start+end)//2
    g = 1 # 공유기
    x = h_list[0]
    idx = 0
    while idx < N-1:
        idx += 1
        if h_list[idx] - x >= mid:
            g += 1
            x = h_list[idx]
    if g >= C: # 거리 늘여도 됨
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)
    