import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n, w = inpl()
    size = 2*n + 1
    visited = [False]*size
    cho = [w+1]

    bsort = inpl()
    cho.extend(bsort)
    cho.extend(inpl())

    bsort.sort(reverse=True)

    cnt = 2 * n
    move = [-1, +1, +n]
    for j in range(1, size):
        if j <= n:
            i = cho.index(bsort[j-1])
        else:
            i = j

        if visited[i]:
            continue
        mem = []
        for mov in move:
            mov = i + mov
            if i <= n:
                if mov == 0:
                    mov = n
                elif mov == n+1:
                    mov = 1
                if 1 <= mov < size:
                    if cho[mov] + cho[i] <= w and visited[mov] == False:
                        mem.append([cho[mov] + cho[i], mov])
            else:
                if mov == n:
                    mov = n*2
                elif mov == 2*n + 1:
                    mov = n+1
                if 1 <= mov <= size:
                    if cho[mov] + cho[i] <= w and visited[mov] == False:
                        mem.append([cho[mov] + cho[i], mov])
        if mem:
            mem.sort(key=lambda x: x[0], reverse=True)
            visited[mem[0][1]] = True
            visited[i] = True
            # print(i, mem[0][1])
            cnt -= 1
    print(cnt)
# testcase

# 1
# 8 100
# 45 45 45 45 45 45 45 45
# 55 55 55 55 55 55 55 55
#
# =>15 but 8
#
# 1
# 4 100
# 100 100 100 100
# 0 0 40 30
#
# =>6 but 5