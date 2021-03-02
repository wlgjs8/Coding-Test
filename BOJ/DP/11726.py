import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n = inp()
a = [0]
dp = [0]

dp.append(1)
dp.append(2)
for i in range(3, n+1):
    dp.append(dp[i-1] + dp[i-2])

print(dp[n] % 10007)
print(dp[n])