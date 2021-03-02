import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [0]
dp = [0 for _ in range(n+1)]
triple = [0 for _ in range(n+1)]

for _ in range(n):
    a.append(inp())

dp[1] = a[1]
# dp[2] = a[1] + a[2]
# dp[3] = max(dp[1], dp[2]) + a[3]
for i in range(2, n+1):
    if triple[i-1] == 1:
        dp[i] = max(dp[i - 2], dp[i - 3]+a[i-1]) + a[i]
        if max(dp[i - 2], dp[i - 3]+a[i-1]) != dp[i-2]:
            triple[i] = 1
    else:
        dp[i] = max(dp[i-1], dp[i-2]) + a[i]
        if max(dp[i-1], dp[i-2]) == dp[i-1]:
            triple[i] = 1

print(dp[n])
print(dp[1:])
print(triple[1:])