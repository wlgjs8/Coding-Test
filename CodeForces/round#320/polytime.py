import sys

a, b = list(map(int, sys.stdin.readline().split()))

if b > a :
    print(-1)
elif b == a:
    print(a)
else:
    t = (a+b)/(2*int((a+b)/b/2))
    print(t)

# minT = 100000001
# for k in range(0, 10000):
#     if k == 0:
#         t = minT
#     else:
#         t = (a - b) / 2 * k
#     if t >= b:
#         if minT > t:
#             minT = t
#
#     t = (a + b) / ( 2 * (k + 1) )
#     if t >= b:
#         if minT > t:
#             minT = t
#
#
#
# print(minT)