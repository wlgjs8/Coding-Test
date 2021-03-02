import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = []
dp = [0] * (n+1)
for _ in range(n):
    a.append(inpl())

for i in range(n):
    # if a[i][0] <= n - i + 1:
    if a[i][0] <= n - i:
        dp[i + a[i][0]] = max(dp[i]+a[i][1], dp[i + a[i][0]])
    dp[i+1] = max(dp[i+1], dp[i])
print(dp[n])
