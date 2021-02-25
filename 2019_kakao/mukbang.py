def solution(food_times, k):
    answer = 0
    cur_food = -1
    no_foodSet = set()

    while k > 0:
        cur_food += 1
        if cur_food == len(food_times):
            cur_food = 0
        if food_times[cur_food] == 0:
            if len(no_foodSet) == len(food_times):
                cur_food = -1
                break
            # print('here', food_times, cur_food)
            no_foodSet.add(cur_food)
            continue

        # print(food_times, cur_food)

        food_times[cur_food] -= 1
        if food_times[cur_food] == 0:
            no_foodSet.add(cur_food)
        k -= 1

    if len(no_foodSet) == len(food_times):
        cur_food = -1

    if cur_food == -1:
        answer = cur_food
    else:
        # print('no_foodSet : ', no_foodSet)
        # print(food_times, cur_food)
        for i in range(len(food_times)):
            cur_food += 1
            if cur_food == len(food_times):
                cur_food = 0
            if food_times[cur_food] != 0:
                answer = cur_food + 1
                break

    return answer

# print(solution([3, 1, 2], 5))
print(solution([3, 1, 2, 1], 5))
# print(solution([0,0,0,0,2,0], 1))
