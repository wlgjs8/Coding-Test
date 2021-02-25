import sys

def inp(): return int(sys.stdin.readline())

t = inp()
for _ in range(t):
    n = inp()
    if n == 1:
        print('NO')
    elif n % 2 == 1:
        print('YES')
    else:
        while True:
            if n == 2:
                print('NO')
                break
            if n % 2 == 1:
                print('YES')
                break
            n = int(n / 2)
