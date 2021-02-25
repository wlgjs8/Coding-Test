def solution(routes):
    routes.sort(key=lambda x:x[1])

    cctvRange = [routes[0][1]]
    for route in routes:
        check = False
        for cctv in cctvRange:
            if cctv >= route[0]:
                check = True
                break
        if not check:
            cctvRange.append(route[1])

    # print(cctvRange)
    answer = len(cctvRange)
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))