import sys

N = int(sys.stdin.readline())

x = list(map(int, sys.stdin.readline().split()))
y = list(map(int, sys.stdin.readline().split()))

max_distance = 0
for i in range(N):
    for j in range(i+1, N):
        nx = (x[i] - x[j]) ** 2
        ny = (y[i] - y[j]) ** 2
        sqr_distance = nx + ny

        if sqr_distance > max_distance:
            max_distance = sqr_distance
    if max_distance == 8000000:
        break

print(max_distance)