
# def solution(number, k):
#     answer = number
#     while k != 0:
#         for i in range(len(answer)-1):
#             print(answer)
#             num1 = int(answer[i])
#             num2 = int(answer[i+1])
#             if num1 < num2:
#                 if i == 0:
#                     answer = answer[i+1:]
#                 else :
#                     answer = answer[0:i] + answer[i+1:]
#                 break
#             if i == (len(answer)-2):
#                 answer = answer[0:i+1]
#         k = k -1
#     return answer

def solution(number, k):
    answer = ''
    numberCopy = number
    lenAnswer = len(number) - k
    while k != 0:
        if len(answer) == lenAnswer:
            break
        maxN = '-1'
        maxI = -1

        for i in range(k+1):
            if number[i] == '9':
                maxN = number[i]
                maxI = i
                break
            # print('number : ', number)
            if maxN < number[i]:
                maxN = number[i]
                maxI = i

        answer = answer + maxN

        number = number[maxI+1:]
        k = k-maxI
        # print(maxN, maxI, answer, k)

    if lenAnswer - len(answer) > 0:
        answer = answer + numberCopy[len(numberCopy) - (lenAnswer - len(answer)):]
    return answer

print(solution('1942', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('9991111', 4))

