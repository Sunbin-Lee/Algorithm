steps = [(-1,0), (1,0), (0,-1), (0,1)]
def find_student(arr, teachers):
    for t_i, t_j in teachers:
        for s in steps:
            new_i = t_i + s[0]
            new_j = t_j + s[1]
            while 0 <= new_i < N and 0 <= new_j < N:
                if arr[new_i][new_j] == 'O':
                    break
                if arr[new_i][new_j] == 'S': # 감시로부터 피하지 못하는 학생 존재
                    return False
                new_i += s[0]
                new_j += s[1]

    return True

def make_wall(arr, teachers, count):
    global answer
    if count == 0:
        if find_student(arr, teachers):
            answer = 'YES'
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                make_wall(arr, teachers, count-1)
                arr[i][j] = 'X'

if __name__ == '__main__':
    N = int(input())
    arr = []
    teachers = []
    for i in range(N):
        row = list(input().split())
        for j in range(N):
            if row[j] == 'T':
                teachers.append((i, j))
        arr.append(row)

    answer = 'NO'
    make_wall(arr, teachers, 3)

    print(answer)
