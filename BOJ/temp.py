import sys

N = sys.stdin.readline().strip()

num_result = [0,0,0,0,0,0,0,0,0,0]
for i in range(1, int(N)+1):
    str_i = str(i)
    for tmp in str_i:
        num_result[int(tmp)] += 1
print(num_result)