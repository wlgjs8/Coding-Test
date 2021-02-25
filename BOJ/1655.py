import sys
from bisect import bisect_left

def inp(): return int(sys.stdin.readline())

n = inp()
nums = list()

new_integer = inp()
nums.append(new_integer)
print(new_integer)

cnt = 1
for _ in range(n-1):
    new_integer = inp()

    index = bisect_left(nums, new_integer)
    nums.insert(index, new_integer)
    cnt += 1

    if cnt % 2 == 0:
        print(min(nums[cnt // 2 -1], nums[cnt//2]))
    else:
        print(nums[cnt//2])