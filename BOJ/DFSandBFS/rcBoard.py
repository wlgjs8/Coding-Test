import sys
sys.setrecursionlimit(10000)

def RC_board(x, y):
    # print('visited_alphabet : ', visited_alphabet)
    global path_cnt, path_max
    path_cnt += 1
    visited_alphabet.add(board[x][y])

    if path_max == 26:
        return

    if path_cnt > path_max:
        path_max = path_cnt

    for i in range(4):
        if board[x+dx[i]][y+dy[i]] != 0 and board[x+dx[i]][y+dy[i]] not in visited_alphabet:
            RC_board(x+dx[i], y+dy[i])

    path_cnt -= 1
    visited_alphabet.remove(board[x][y])

    return

R, C = list(map(int, sys.stdin.readline().split()))
board = [[0] * (C+2) for _ in range(R+2)]

for row in range(R):
    str = sys.stdin.readline()
    # print(str[1])
    for col in range(C):
        board[row+1][col+1] = str[col]

# board = [[0, 0, 0, 0, 0, 0], [0, 'C', 'A', 'A', 'B', 0], [0, 'A', 'D', 'C', 'B', 0], [0, 0, 0, 0, 0, 0]]
visited_alphabet = set()
global path_cnt
path_cnt = 0
global path_max
path_max = 0

dx = [0, 1, 0, -1]
dy = [1,0,-1,0]

RC_board(1, 1)
print(path_max)
