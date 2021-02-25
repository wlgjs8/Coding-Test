import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

M = inp()
N = inp()

sosu = []

for i in range(2, max(M,N)+1):
    check = True
    for j in range(2, i):
        if i % j == 0 and j != 1:
            check = False
            break
    if check:
        sosu.append(i)
min = 10000
sum = 0
for i in range(M, N+1):
    if i in sosu:
        sum += i
        if min > i:
            min = i

if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)