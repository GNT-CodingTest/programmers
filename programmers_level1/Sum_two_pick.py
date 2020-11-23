
# 기댓값
# https://programmers.co.kr/learn/courses/30/lessons/68644
# [2,3,4,5,6,7]
# [2,5,7,9,12]

# 100/100
def solution(numbers):
    answer = []
    for key1, value1 in enumerate(numbers[:len(numbers)-1]):  # 2, 1, 3, 4
        for key2, value2 in enumerate(numbers[key1 + 1:]):  # key1이 0일때 1, 3, 4, 1 / key1이 1일때 3, 4, 1
            if (value1 + value2) not in answer:
                answer.append(value1 + value2)
    answer.sort()

    return answer


# Error
# def solution(numbers):
#     answer = []
#     temp = []
#     for key1, value1 in enumerate(numbers[:len(numbers)-1]):  # 2, 1, 3, 4
#         for key2, value2 in enumerate(numbers[key1 + 1:]):  # key1이 0일때 1, 3, 4, 1 / key1이 1일때 3, 4, 1
#             answer.append(value1 + value2)
#
#     temp = set(answer)
#
#     return sorted(temp)

# 다른사람 풀이 인상깊은 풀이

# def solution(numbers): return sorted({numbers[i] + numbers[j]
#                                       for i in range(len(numbers)-1) for j in range(len(numbers)-1) if i > j})


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
