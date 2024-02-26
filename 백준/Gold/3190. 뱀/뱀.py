from collections import deque

N = int(input())
K = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    apple_x, apple_y = map(int, input().split())
    arr[apple_x-1][apple_y-1] = 2

L = int(input())
commands = []
for _ in range(L):
    t, d = input().split()
    if d == 'L':
        d = -1
    else:
        d = 1
    commands.append((int(t), d))

steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]

start_x, start_y = 0, 0
q = deque([(start_x, start_y)])
arr[start_x][start_y] = 1

start_d = 0 # 방향
time = 0

while True:
    time += 1

    new_x = start_x + steps[start_d][0]
    new_y = start_y + steps[start_d][1]

    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
        break
    if arr[new_x][new_y] == 1:
        break

    q.append((new_x, new_y))
    if arr[new_x][new_y] == 0:
        x, y = q.popleft()
        arr[x][y] = 0

    arr[new_x][new_y] = 1
    start_x, start_y = new_x, new_y

    if commands and time == commands[0][0]: # 다음 턴의 방향 정하기
        start_d += commands[0][1]
        start_d = start_d % 4
        commands.pop(0)

print(time)
