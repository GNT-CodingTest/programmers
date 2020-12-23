from collections import deque


def solution(numbers):
    answer = 0

    num_list = deque()
    for number in numbers:
        num_list.append(number)

    num_set = set(map(int, test(num_list)))
    print(num_set)

    sieve = eratosthenes_sieve(max(num_set))

    for num in num_set:
        if num in sieve:
            answer += 1

    return answer


def test(num_list):

    x = set()
    for i in range(len(num_list)):
        y = []
        temp = num_list.popleft()
        x.add(temp)

        if num_list:
            y.extend(test(num_list.copy()))
        else:
            return temp

        for z in y:
            x.add(temp + z)

        num_list.append(temp)

    return x


def eratosthenes_sieve(n):
    answer = set(range(2, n+1))

    for value in range(2, n+1):
        if value in answer:
            answer -= set(range(value * 2, n + 1, value))
    return answer


print(solution('17'))
print(solution('011'))
# print(solution('123'))


# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)

# import itertools
#
# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기