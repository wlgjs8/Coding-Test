from itertools import permutations

def remove(string, index):
    return string[0:index] + string[index+1:]

def idCompare(userID, banID):
    starList = []
    for i in range(len(banID)):
        if banID[i] == '*':
            starList.append(i)
    for i in reversed(range(len(starList))):
        userID = remove(userID, starList[i])
        banID = remove(banID, starList[i])

    if banID == userID:
        return True
    else:
        return False

def solution(user_id, banned_id):
    cntList = [0 for jk in range(9)]
    for i in range(1, 9):
        userList = []
        banList = []
        for userID in user_id:
            if len(userID) == i:
                userList.append(userID)
        for banID in banned_id:
            if len(banID) == i:
                banList.append(banID)

        userAllCase = list(permutations(userList, len(banList)))

        if userAllCase :
            if userAllCase[0] != ():
                answerList = []
                for userCase in userAllCase:
                    flag = 1
                    for j in range(len(banList)):
                        if idCompare(userCase[j], banList[j]) == False:
                            flag = 0
                    if flag == 1:
                        cntList[i] = cntList[i] + 1
                        answerList.append(userCase)
                answerListCopy = answerList.copy()
                for index in range(len(answerList) - 1):
                    for index2 in range(index + 1, len(answerList)):
                        if set(answerList[index]) == set(answerList[index2]):
                            # answerListCopy.remove(answerList[index2])
                            # del(answerListCopy[index2])
                            # index2 = index2 - 2
                            # print(answerListCopy[index2])
                            cntList[i] = cntList[i] - 1
    # print(answerListCopy)
    # print(cntList)
    answer = 0
    for i in cntList:
        if i != 0:
            if answer == 0:
                answer = 1
            answer = answer * i
    return answer


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "fr*d*"]))
# print(solution(["f1"],["f*"]))
# print(solution(["f11", "f21", "f32", "f42"], ["f*1", "f**", "f**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
