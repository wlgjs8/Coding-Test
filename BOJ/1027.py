import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N = inp()
building = [-1]
building.extend(inpl())
# print(building)

MAX = 0
for i in range(1, N + 1):
    cnt = 0
    for j in range(1, N + 1):
        check = True
        if i == j: continue
        elif i - j >= 2:
            for k in range(j+1, i):
                m = k-j
                n = i-k
                bet = (building[i] * m + building[j] * n) / (m + n)
                if building[k] >= bet:
                    check = False
                    break
            if check:
                cnt += 1
            # print('left : ', i, j, cnt, bet, building[k])
        elif j - i >= 2:
            for k in range(i+1, j):
                m = k-i
                n = j-k
                bet = (building[i] * n + building[j] * m) / (m + n)
                # print(i, j, k, bet)
                if building[k] >= bet:
                    check = False
                    break
            if check:
                cnt += 1
            # print('right : ', i, j, cnt, bet, building[k])
        else:
            cnt += 1
    # print('= total :', i,j, cnt)
    if cnt > MAX:
        MAX = cnt
print(MAX)