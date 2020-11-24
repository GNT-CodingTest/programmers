import timeit
import collections


def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]

    return participant[-1]


def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


def solution3(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    # 1, 2, 3, 4 를 더하고

    for com in completion:
        temp -= hash(com)
    # 1, 3, 4 를 빼면

    answer = dic[temp]
    # 2를 반환

    return answer


startTime = timeit.default_timer()

print(solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
print(solution(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))

endTime = timeit.default_timer()

print(f"{endTime - startTime}초")


# startTime = timeit.default_timer()
#
# print(solution3(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
# print(solution3(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina', 'nikola']))
# print(solution3(['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))
#
# endTime = timeit.default_timer()
#
# print(f"{endTime - startTime}초")
