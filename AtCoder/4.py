import sys
def num_system(num, base):
    num = str(num)
    answer = 0
    for i in range(len(num)-1, -1, -1):
        answer += int(num[len(num) - 1 - i]) * base ** i
    return answer

def inp(): return int(sys.stdin.readline())

str_x = sys.stdin.readline()
m = inp()

int_x = int(str_x)
big_x = 0
for i in range(len(str_x)-2, -1, -1):
    xx = int_x // (10**i)
    int_x = int_x % (10**i)
    if big_x < xx:
        big_x = xx
i = big_x + 1
cnt = 0
int_x = int(str_x)
while True:
    num = num_system(int_x, i)
    if num > m:
        break
    cnt += 1
    i += 1
print(cnt)
