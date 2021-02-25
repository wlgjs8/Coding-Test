import sys

N = sys.stdin.readline().strip()
zarit = [1]
zarit0 = [0]
sum = 1
sum0 = 0
for i in range(1, len(N)):
    temp = (10**i + sum) + sum * 8
    zarit.append(temp)
    sum += zarit[i]
    temp = ((10**i) * 9 * (i+1)) - zarit[i] * 9
    zarit0.append(temp)
    sum0 += zarit0[i]

num_result = []
num_result.append(sum0-zarit0[len(N)-1])
for _ in range(9):
    num_result.append(sum-zarit[len(N)-1])

lenn = ''
for i in range(1, len(N)):
    lenn += '9'
if len(N) > 1:
    lennn = int(lenn) + 1
else:
    lennn = 1
for i in range(lennn, int(N)+1):
    str_i = str(i)
    for tmp in str_i:
        num_result[int(tmp)] += 1

print(*num_result)
