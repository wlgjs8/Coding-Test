import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

for N in range(1, 101):
    # N = inp()
    print(N, ' : ', end=' ')
    comb = set()
    NN = N
    ans = []

    i = 2
    cnt = 0
    while N != 1:
        if N % i == 0:
            N //= i
            if cnt % 2 == 0:
                ans.append(i)
            else:
                ans[cnt // 2] *= i
            cnt += 1
        else:
            i += 1
    if len(ans) > 1:
        if ans[len(ans) - 1] < 4:
            ans[len(ans) - 2] *= ans[len(ans) - 1]
            del ans[len(ans) - 1]

    if len(ans) > 1 and cnt > 3:
        print(*ans)
    else:
        print(-1)