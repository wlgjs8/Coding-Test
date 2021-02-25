import sys

t = int(sys.stdin.readline())

x_list = list()
y_list = list()

for _ in range(t):
    x, y = list(map(int, sys.stdin.readline().split()))

    i = 1
    sum = 0
    while i*i <= x:
        # print(int((x-i)/i), y)
        m = min((x-i)/i,y)
        sum += int(max(0, m - i))
        i+= 1
    print(sum)