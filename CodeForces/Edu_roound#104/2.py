import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, k = list(map(int, sys.stdin.readline().split()))

    cnt = k
    if n % 2 != 0 :
        T = n // 2
        if k >= (T+1):
            cnt += 1
            cnt += (k - T - 1) // T

    print(((cnt-1) % n) + 1)