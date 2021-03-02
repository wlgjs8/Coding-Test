import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

N, M, D = inpl()
a = []
INF = -10000000000
dp = [[INF] * M for _ in range(N)]
for _ in range(N):
    a.append(inpl())
for i in range(M):
    dp[0][i] = 0

for i in range(N):
    for j in range(M):
        for ii in range(1, D+1):
            for jj in range(-D+1, D):
                if abs(ii) + abs(jj) <= D:
                    nx = i + ii
                    ny = j + jj

                    if 0 <= nx < N and 0 <= ny < M:
                        dp[nx][ny] = max(dp[nx][ny], a[i][j] * a[nx][ny] + dp[i][j])
MAX = max(dp[N-1])
print(MAX)