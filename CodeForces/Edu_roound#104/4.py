import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    if n < 4:
        print(0)
    else:
        n -= 1
        a = int((2*n + 1) ** 0.5)
        if a % 2 == 0:
            a -= 1
        a = (a-3) // 2 + 1
        print(a)