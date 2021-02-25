import sys
N, X = list(map(int, sys.stdin.readline().split()))
a = list(map(int, sys.stdin.readline().split()))

sum = 0
a.sort()

cnt = 0
for i in range(N):
    sum += a[i]
    if sum > X:
        break
    cnt += 1

print(cnt)