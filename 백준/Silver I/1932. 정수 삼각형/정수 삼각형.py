n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))

dp_table = [[0 for _ in range(n)] for _ in range(n)]
dp_table[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp_table[i][j] = dp_table[i-1][j] + triangle[i][j]
        elif j == i:
            dp_table[i][j] = dp_table[i-1][j-1] + triangle[i][j]
        else:
            dp_table[i][j] = max(dp_table[i-1][j], dp_table[i-1][j-1]) + triangle[i][j]

print(max(dp_table[-1]))