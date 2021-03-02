import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, K = inpl()
a = inpl()
finalK = [i for i in range(1, N+1)]

check = False
for i in range(K, N+1):
    if set(a[:i]) == set(finalK[:i]):
        check = True
        break

cnt = 0
if not check:
    alreadyhas = 1
    a = a[N - 1:] + a[:N - 1]
    check2 = True
    while check2:
        while True:
            if alreadyhas not in a:
                a.insert(0, alreadyhas)
                cnt += 1
                break
            else:
                alreadyhas += 1
        index1 = a.index(1)
        for c in range(K, N+1):
            if set(a[:c]) == set(finalK[:c]):
                check2 = False
                break

print(cnt)
