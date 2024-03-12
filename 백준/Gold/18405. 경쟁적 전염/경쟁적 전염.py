steps = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def spread_virus(map_arr, virus):
    update_v = []
    while virus:
        v, i, j = virus.pop()
        for s in steps:
            new_i = i + s[0]
            new_j = j + s[1]
            if new_i < 0 or new_i >= N or new_j < 0 or new_j >= N:
                continue
            if map_arr[new_i][new_j] == 0:
                map_arr[new_i][new_j] = v
                update_v.append((v, new_i, new_j))
    return update_v

if __name__ == '__main__':
    N, K = map(int, input().split())
    map_arr = []
    virus = [] # virus
    for i in range(N):
        row = list(map(int, input().split()))
        for j in range(N):
            if row[j] > 0:
                virus.append((row[j], i, j))
        map_arr.append(row)
    S, X, Y = map(int, input().split())

    for _ in range(S):
        virus.sort(reverse=True)
        virus = spread_virus(map_arr, virus)

    print(map_arr[X-1][Y-1])