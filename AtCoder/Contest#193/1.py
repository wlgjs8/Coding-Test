import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

# N = inp()

t = inp()
for _ in range(t):
    check = False
    x, y, p, q = inpl()
    i = 0;

    if 2 * (x+y) == p + q:
        print('infinity')
        continue

    i = 0
    while True:
        start = x + 2 * i *(x+y)
        end = start + y
        s = p
        e = s + q

        if s > end:
            i+=1
            continue
        while e < end:

            # if i < 3:
                # print('hh : ', s, e)
            for j in range(s, e):
                if start <= j < e:
                    print(j)
                    check = True
                    break
            if check:
                break
            s = e + p
            e = s + q
        if check:
            break
        i += 1