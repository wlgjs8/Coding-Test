def solution(record):
    answer = []
    userInfo = {}

    for str in record:
        stuff = str.split()

        if stuff[0] == "Enter" or stuff[0] == "Change":
            userInfo[stuff[1]] = stuff[2]

    for str in record:
        stuff = str.split(' ')

        if stuff[0] == 'Enter':
            cur_record = userInfo[stuff[1]]+'님이 들어왔습니다.'
        elif stuff[0] == 'Leave':
            cur_record = userInfo[stuff[1]]+'님이 나갔습니다.'
        else:
            continue
        answer.append(cur_record)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
# print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan", "Change uid4567 wlgjs"]))