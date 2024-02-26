from collections import deque

N = int(input())
map_arr = [[False for _ in range(N)] for _ in range(N)]
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    map_arr[a-1][b-1] = True

commands = deque([])
L = int(input())
for _ in range(L):
    X, C = input().split()
    commands.append((int(X), C))

snakes = deque([(0, 0)])
steps = [(0,1), (1,0), (0,-1), (-1,0)]
d = 0
T = 0
while True:
    if commands and T == commands[0][0]:
        X, C = commands.popleft()
        if C == 'D':
            d = (d+1)%4
        elif C == 'L':
            d = (d+3)%4

    T += 1
    head_i, head_j = snakes[-1]

    next_i = head_i + steps[d][0]
    next_j = head_j + steps[d][1]
    if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N: # 벽
        break
    if (next_i, next_j) in snakes: # 몸통
        break
    snakes.append((next_i, next_j))

    if map_arr[next_i][next_j]: # 사과
        map_arr[next_i][next_j] = False
    else:
        snakes.popleft()

print(T)