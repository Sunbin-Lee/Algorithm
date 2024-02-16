N = int(input())
s_list = list(map(int, input().split()))

dp_table = [1 for _ in range(N)]
for i in range(1, N):
    for j in range(i):
        if s_list[j] > s_list[i]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)

print(N - max(dp_table))