import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

dp = [1 for _ in range(n)]
# print(dp)
for i in range(1, n):
    s = []
    for j in range(i):
        if a[i] < a[j]:
            s.append(dp[j])
    if s:
        dp[i] += max(s)

print(max(dp))