import sys

N = int(sys.stdin.readline())
members = list()
list_sum = list()
for i in range(2*N-1):
     members.append(list(map(int, sys.stdin.readline().split())))
     for j in range(len(members[i])):
        list_sum.append([members[i][j], (i+2,j+1)])

list_sum.sort(key=lambda x: x[0], reverse=True)

members_set = set()
teammates = [0] * 2*N

for one_list in list_sum:
    if N == 0:
        break

    elif one_list[1][0] not in members_set and one_list[1][1] not in members_set:
        members_set.add(one_list[1][0])
        members_set.add(one_list[1][1])
        teammates[one_list[1][0]-1] = one_list[1][1]
        teammates[one_list[1][1]-1] = one_list[1][0]
        N -= 1
        continue

print(' '.join(repr(e) for e in teammates))