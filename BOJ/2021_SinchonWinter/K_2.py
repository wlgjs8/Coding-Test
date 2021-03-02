import sys

N = int(sys.stdin.readline())
ans = []

i = 2
while N >= i**2:
    if N % (i**2) == 0:
        N //= i**2
        ans.append(i**2)
    else:
        i += 1
check = False
for i in range(4, N):
    if N % i == 0:
        check = True
        ans.append(N)
        break
if not check:
    ans[len(ans)-1] *= N
if len(ans) > 1:
    print(*ans)
else:
    print(-1)