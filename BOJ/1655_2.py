import sys
import heapq

def inp(): return int(sys.stdin.readline())

left, right = list(), list()
n = inp()

for _ in range(n):
    num = inp()
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))
    else:
        heapq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        left_value = heapq.heappop(left)[1]
        right_value = heapq.heappop(right)[1]
        heapq.heappush(right, (left_value, left_value))
        heapq.heappush(left, (-right_value, right_value))
    # print(left, ' vs ', right)
    print(left[0][1])