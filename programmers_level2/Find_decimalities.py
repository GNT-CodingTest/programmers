from collections import deque


def solution(numbers):
    answer = 0

    num_list = deque()
    for number in numbers:
        num_list.append(number)

    num_set = set(map(int, dfs(num_list)))
    print(num_set)

    sieve = eratosthenes_sieve(max(num_set))

    for num in num_set:
        if num in sieve:
            answer += 1

    return answer


def dfs(num_list):

    x = set()
    for i in range(len(num_list)):
        y = []
        temp = num_list.popleft()
        x.add(temp)

        if num_list:
            y.extend(dfs(num_list.copy()))
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
# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
# permutations(range(3)) --> 012 021 102 120 201 210

# 어떤 자연수 n이 소수임을 판정하기 위해서 # |√n|까지만 진행하면 되는데,
# 수가 수를 나누기 위해서는 그 몫이 항상 필요하며
# 나누는 수와 몫 중 어느 하나는 반드시 √n 이하이기 때문이다.
