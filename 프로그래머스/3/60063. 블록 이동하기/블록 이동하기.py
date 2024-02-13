from collections import deque

def solution(board):
    N = len(board)
    q = deque([(0, 1, 0, 0)]) # (오른쪽 아래) x, y, dir, time
    
    visited_0 = [[0 for _ in range(N)] for _ in range(N)]
    visited_1 = [[0 for _ in range(N)] for _ in range(N)]
    
    visited_0[0][1] = 1 
    
    while q:
        # print(q)
        x, y, d, t = q.popleft()
        if x == N-1 and y == N-1:
            break
        
        if d == 0: # 가로
            if y-2 >= 0 and board[x][y-2] == 0:
                if visited_0[x][y-1] == 0:
                    q.append((x, y-1, 0, t+1))
                    visited_0[x][y-1] = 1
            
            if y+1 < N and board[x][y+1] == 0:
                if visited_0[x][y+1] == 0:
                    q.append((x, y+1, 0, t+1)) # 오른쪽
                    visited_0[x][y+1] = 1
                    
            if x+1 < N and board[x+1][y-1] == 0 and board[x+1][y] == 0:
                if visited_0[x+1][y] == 0:
                    q.append((x+1, y, 0, t+1)) # 아래
                    visited_0[x+1][y] = 1
                    
                if visited_1[x+1][y] == 0:
                    q.append((x+1, y, 1, t+1)) # 회전
                    visited_1[x+1][y] = 1
                if visited_1[x+1][y-1] == 0:
                    q.append((x+1, y-1, 1, t+1)) # 회전
                    visited_1[x+1][y-1] = 1
                    
            if x-1 >= 0 and board[x-1][y-1] == 0 and board[x-1][y] == 0:
                if visited_0[x-1][y] == 0:
                    q.append((x-1, y, 0, t+1)) # 위
                    visited_0[x-1][y] = 1
                
                if visited_1[x][y] == 0:
                    q.append((x, y, 1, t+1)) # 회전
                    visited_1[x][y] = 1
                if visited_1[x][y-1] == 0:
                    q.append((x, y-1, 1, t+1))
                    visited_1[x][y-1] = 1
                    
        elif d == 1: # 세로
            if x-2 >= 0 and board[x-2][y] == 0:
                if visited_1[x-1][y] == 0:
                    q.append((x-1, y, 1, t+1))
                    visited_1[x-1][y] = 1
            
            if x+1 < N and board[x+1][y] == 0:
                if visited_1[x+1][y] == 0:
                    q.append((x+1, y, 1, t+1)) # 아래
                    visited_1[x+1][y] = 1
                    
            if y+1 < N and board[x-1][y+1] == 0 and board[x][y+1] == 0:
                if visited_1[x][y+1] == 0:
                    q.append((x, y+1, 1, t+1)) # 오른쪽
                    visited_1[x][y+1] = 1
                    
                if visited_0[x][y+1] == 0:
                    q.append((x, y+1, 0, t+1)) # 회전
                    visited_0[x][y+1] = 1
                if visited_0[x-1][y+1] == 0:
                    q.append((x-1, y+1, 0, t+1)) # 회전
                    visited_0[x-1][y+1] = 1
                    
            if y-1 >= 0 and board[x-1][y-1] == 0 and board[x][y-1] == 0:
                if visited_1[x][y-1] == 0:
                    q.append((x, y-1, 1, t+1))
                    visited_1[x][y-1] = 1
                
                if visited_0[x][y] == 0:
                    q.append((x, y, 0, t+1)) # 회전
                    visited_0[x][y] = 1
                if visited_0[x-1][y] == 0:
                    q.append((x-1, y, 0, t+1))
                    visited_0[x-1][y] = 1
                
    return t