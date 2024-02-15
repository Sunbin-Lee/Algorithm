N = int(input())
consults = [0]
for _ in range(N):
    consults.append((tuple(map(int, input().split()))))

# 해당 날짜부터 N일까지 최대 수익 저장
dp_table = [0 for _ in range(N+2)]
for i in range(N, 0, -1):
    if i + consults[i][0] > N+1: # 해당 날짜의 상담을 진행할 수 없는 경우
        dp_table[i] = dp_table[i+1]
    else: # 진행할 수 있는 경우
        dp_table[i] = max(dp_table[i+1], dp_table[i+consults[i][0]] + consults[i][1])

print(dp_table[1])