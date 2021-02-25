import math

def div(a):
    return math.ceil(a/2)

def big(a, b):
    if a > b:
        return a
    else:
        return b

def solution(n,a,b):
    cnt = 1
    while 1:
        result = abs(b - a)
        if (result == 1) & (big(a, b) % 2 == 0):
            answer = cnt
            break
        else:
            cnt = cnt + 1
            a = div(a)
            b = div(b)

    return answer

# print(solution(8, 4, 7))
print(solution(32, 2, 5))