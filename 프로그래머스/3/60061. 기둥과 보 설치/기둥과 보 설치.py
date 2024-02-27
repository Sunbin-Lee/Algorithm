def check(map_arr, x, y, a):
    n = len(map_arr[0])
    if a == 0: # 기둥
        if y == 0: # 바닥 위
            return True
        if map_arr[0][x][y-1] == 1: # 다른 기둥 위
            return True
        if (x > 0 and map_arr[1][x-1][y] == 1) or map_arr[1][x][y] == 1: # 보
            return True
        return False
    if a == 1: # 보
        if y == 0:
            return False
        if map_arr[0][x][y-1] == 1 or (x < n-1 and map_arr[0][x+1][y-1] == 1): # 기둥
            return True
        if 0 < x < n-1 and map_arr[1][x-1][y] == 1 and map_arr[1][x+1][y] == 1: # 보
            return True
        return False
        
def solution(n, build_frame):
    map_arr = [[[0 for _ in range(n+1)] for _ in range(n+1)] for _ in range(2)]

    answer = []
    for x, y, a, b in build_frame:
        if b == 1: # 설치
            if check(map_arr, x, y, a):
                answer.append([x, y, a])
                map_arr[a][x][y] = 1
        elif b == 0: # 삭제
            map_arr[a][x][y] = 0
            
            delete = True
            for xi, yi, ai in answer:
                if not check(map_arr, xi, yi, ai):
                    delete = False
                    break
                    
            if delete:
                answer.remove([x, y, a])
            else:
                map_arr[a][x][y] = 1

    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    
    return answer