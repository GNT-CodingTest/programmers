import itertools


def solution1(number, k):
    combinations = list(map(''.join, itertools.combinations(number, len(number) - k)))

    return max(combinations)


def solution(number, k):
    num_list = list(map(int, number))
    _len = len(number) - k

    max_num = max_sieve(num_list, _len)
    # max_num = min_sieve(num_list, k)

    return ''.join(list(map(str, max_num)))


def max_sieve(num_list, max_len):
    max_num = []
    idx = num_list.index(max(num_list))

    temp = []
    if max_len <= len(num_list[idx:]):
        del (num_list[:idx])
        temp = min_sieve(num_list, len(num_list) - max_len)
    else:
        max_num.extend(num_list[idx:])
        del (num_list[idx:])
        temp = max_sieve(num_list, max_len - len(max_num))

    if max_num:
        temp.extend(max_num)

    return temp


def min_sieve(num_list, del_cnt):
    cnt = 0
    while 1:
        if del_cnt == cnt:
            break

        idx = num_list.index(min(num_list))
        del(num_list[idx])
        cnt += 1

    return num_list


print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
