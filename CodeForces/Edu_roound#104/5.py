import sys
INF = float('inf')

def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

first_course_size, second_course_size, drink_size, dessert_size = inpl()

first_course = inpl()
second_course = inpl()
drink_course = inpl()
dessert_course = inpl()

N = inp()
first_second = [inpl() for _ in range(N)]
N = inp()
second_drink = [inpl() for _ in range(N)]
N = inp()
drink_dessert = [inpl() for _ in range(N)]

min_cost = INF
que = list()
for first in first_course:
    que.append([first, 0, first])

while que:
    menu_list = que.pop(0)

    if menu_list[1] == 0:
        for second in range(second_course_size):
            if [menu_list[2], second+1] not in first_second:
                que.append([menu_list[0]+second_course[second], 1, second+1])

    elif menu_list[1] == 1:
        for drink in range(drink_size):
            if [menu_list[2], drink+1] not in second_drink:
                que.append([menu_list[0] + drink_course[drink], 2, drink+1])

    elif menu_list[1] == 2:
        for dessert in range(dessert_size):
            if [menu_list[2], dessert+1] not in drink_dessert:
                que.append([menu_list[0] + dessert_course[dessert], 3, dessert+1])

    elif menu_list[1] == 3:
        if menu_list[0] < min_cost:
            min_cost = menu_list[0]

if min_cost == INF:
    min_cost = -1
print(min_cost)
