import sys

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

t = inp()
for _ in range(t):
    n = inp()
    dotX = list()
    dotY = list()

    avgX, avgY = 0, 0
    for _ in range(n):
        x, y = inpl()
        avgX += x
        avgY += y
        dotX.append(x)
        dotY.append(y)

    avgX, avgY = int(avgX / n), int(avgY / n)
    cntX, cntY = 0, 0
    for i in range(n):
        if dotX[i] > avgX:
            cntX += 1
        if dotY[i] < avgY:
            cntY += 1
    if cntX >= int(n / 2):
        bigX, smaX = max(dotX), avgX
    else:
        bigX, smaX = avgX, min(dotX)
    if cntY >= int(n / 2):
        bigY, smaY = max(dotY), avgY
    else:
        bigY, smaY = avgY, min(dotY)
    # bigX, bigY = max(dotX), max(dotY)
    # smaX, smaY = min(dotX), min(dotY)

    min_distance = 1000000001
    cnt = 1
    for x in range(smaX, bigX + 1):
        for y in range(smaY, bigY + 1):
            distance = 0
            for i in range(n):
                distance += abs(x-dotX[i]) + abs(y-dotY[i])
                if distance > min_distance:
                    break

            if distance < min_distance:
                cnt = 1
                min_distance = distance
            elif distance == min_distance:
                cnt += 1

    print(cnt)
