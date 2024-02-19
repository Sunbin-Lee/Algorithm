N = input()
left, right = 0, 0
for i in range(len(N)//2):
    left += int(N[i])
    right += int(N[i+len(N)//2])

if left == right:
    print('LUCKY')
else:
    print('READY')