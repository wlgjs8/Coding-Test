def combi(temp, number, calculate):
    global result
    if len(temp) == len(calculate):
        temp = set(temp)
        if temp not in result:
            result.append(temp)
            print('result : ', result)
        return
    else:
        for j in range(len(calculate[number])):
            if calculate[number][j] not in temp:
                temp.append(calculate[number][j])
                print('temp : ', temp)
                combi(temp, number+1, calculate)
                temp.pop()


#Main start point
result = []
def solution(user_id, banned_id):
    global result
    calculate = []
    for ban in banned_id:
        possible=[]
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                count = 0
                for i in range(len(ban)):
                    if user[i] == ban[i]:
                        count+=1
                if count == len(ban)-ban.count('*'):
                    possible.append(user)
        calculate.append(possible)

    print('calculate : ', calculate)
    combi([], 0, calculate)
    return len(result)

# print(solution(["f11", "f21", "f32", "f42"], ["f*1", "f**", "f**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
print(solution(["crodo", "fradi", "frodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
