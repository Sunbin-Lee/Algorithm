def rotate_90(key, M):
    rotate_key = [[0 for _ in range(M)] for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotate_key[j][M-i-1] = key[i][j]
    return rotate_key

def check(lock_map, N):
    for i in range(N,2*N):
        for j in range(N,2*N):
            if lock_map[i][j] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    
    lock_map = [[0 for _ in range(3*N)] for _ in range(3*N)]
    for i in range(N):
        for j in range(N):
            lock_map[i+N][j+N] = lock[i][j]

    for _ in range(4):
        key = rotate_90(key, M)
        for start_i in range(1,2*N):
            for start_j in range(1,2*N):
                
                for i in range(M):
                    for j in range(M):
                        lock_map[start_i+i][start_j+j] += key[i][j]
                      
                if check(lock_map, N): # if True
                    return True
                        
                for i in range(M):
                    for j in range(M):
                        lock_map[start_i+i][start_j+j] -= key[i][j]
                        
    return False