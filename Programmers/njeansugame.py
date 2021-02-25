import sys
sys.setrecursionlimit(100000)

NOTATION = '0123456789ABCDEF'

def numeral_system(number, base):
    q, r = divmod(number, base)
    n = NOTATION[r]
    return numeral_system(q, base) + n if q else n

def solution(n, t, m, p):
    stringLen = m*t - (m-p)
    str = ''
    answer = ''

    for i in range(100000):
        if len(str) >= stringLen:
            break
        str = str + numeral_system(i, n)

    for i in range(t):
        answer = answer + str[i*m + (p-1)]

    return answer

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))
