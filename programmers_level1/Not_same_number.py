# def solution(arr):
#     answer = []
#
#     temp = -1
#     for i in range(len(arr)):
#         # if arr[i] not in answer:
#         #     answer.append(arr[i])
#         if arr[i] != temp:
#             answer.append(arr[i])
#             temp = arr[i]
#
#     return answer
#
#
# print(solution([1, 1, 3, 3, 0, 1, 1]))
# print(solution([4, 4, 4, 3, 3]))


def no_continuous(s):
    a = []
    for i in s:
        # a[-1:] => list 그래서 i를 리스트 형식으로 만듬
        if a[-1:] == [i]: continue
        # # 리스트 형식이 아니면 인덱스 오버
        # if a[-1] == i: continue
        a.append(i)
    return a


print(no_continuous([1, 1, 3, 3, 0, 1, 1]))
