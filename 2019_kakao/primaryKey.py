from itertools import combinations

def solution(relation):
    answer = 0
    combiList = []
    uniqueIndex = []

    rowSize = len(relation)
    colSize = len(relation[0])

    for i in range(1,colSize+1):
        combiList.extend([set(k) for k in combinations([j for j in range(colSize)], i)])

    for combi in combiList:
        vaildSet = set()
        for row in range(rowSize):
            temp = ''
            # temp = []
            for col in combi:
                temp += relation[row][col]
            vaildSet.add(temp)

        if len(vaildSet) == rowSize:
            uniqueIndex.append(combi)

    delSet = set()
    for stdMinElem in uniqueIndex:
        for compMinElem in uniqueIndex:
            if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
                delSet.add(uniqueIndex.index(compMinElem))

    answer = len(uniqueIndex) - len(delSet)
    return answer
# print(solution([["100","ryan","music","2"],["200","apeach","math","2"]]))
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
