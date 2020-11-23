# def solution(numbers):
#     answer = []
#
#     for i in range(len(numbers)-1):
#         for j in range(i, len(numbers)):
#             temp = numbers[i] + numbers[j]
#             answer.append(temp)
#
#     answer.sort()
#     return answer
#
#
# print(solution([2, 1, 3, 4, 1]))
# print(solution([5, 0, 2, 7]))

# def solution(numbers):
#     answer = []
#
#     for key1, val1 in enumerate(numbers[:len(numbers)-1]):
#         for key2, val2 in enumerate(numbers[key1+1:]):
#             temp = val1+val2
#             if temp not in answer:
#                 answer.append(temp)
#
#     answer.sort()
#     return answer

def solution(numbers):
    answer = []

    for key1, val1 in enumerate(numbers[:len(numbers)-1]):
        for key2, val2 in enumerate(numbers[key1+1:]):
            answer.append(val1+val2)

    temp = set(answer)
    return sorted(temp)


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))