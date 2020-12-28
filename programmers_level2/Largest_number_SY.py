def solution(numbers):
    answer = ''

    num_list = list(map(lambda x: str(x), numbers))
    # num_list = list(map(lambda x: int(x.ljust(4, x[-1])), num_list))

    dic = {}
    for a, b in zip(num_list, numbers):
        if a[0] in dic:
            dic[a[0]].append(b)
        else:
            dic[a[0]] = [b]
    # print(dic)

    for a in dic:
        values = dic[a]

        for i in range(len(values)-1):
            min_idx = i
            for j in range(i+1, len(values)):
                if values[i] > values[j]:
                    min_num_idx = j
                    max_num_idx = i
                else:
                    min_num_idx = i
                    max_num_idx = j
                min_num = values[min_num_idx]
                max_num = values[max_num_idx]

                if str(min_num)[0] > str(max_num)[-1]:
                    min_idx = max_num_idx

            temp = values[i]
            values[i] = values[min_idx]
            values[min_idx] = temp

        dic[a] = values
    # print(dic)

    sort_key = sorted(dic)

    for _ in range(len(sort_key)):
        val = dic[sort_key.pop()]

        for _ in range(len(val)):
            answer += str(val.pop())

    return str(int(answer))


def solution1(numbers):
    answer = ''

    num_list = list(map(lambda x: str(x), numbers))
    num_list = list(map(lambda x: int((x*4)[:4]), num_list))

    dic = {}
    for a, b in zip(num_list, numbers):
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]

    sort_key = sorted(dic)

    for _ in range(len(sort_key)):
        temp = dic[sort_key.pop()]

        for num in temp:
            answer += str(num)

    return str(int(answer))


print(f'{"solution":15}{"solution1"}')
print(f'{solution([6, 10, 2]):15}{solution1([6, 10, 2])}')
print(f'{solution([3, 30, 34, 5, 9]):15}{solution1([3, 30, 34, 5, 9])}')
print(f'{solution([10, 101]):15}{solution1([10, 101])}')
print(f'{solution([101, 10]):15}{solution1([101, 10])}')
print(f'{solution([0, 0, 0, 0, 0, 0]):15}{solution1([0, 0, 0, 0, 0, 0])}')
print(f'{solution([1, 11, 111, 1111]):15}{solution1([1, 11, 111, 1111])}')
print(f'{solution([40, 403]):15}{solution1([40, 403])}')
print(f'{solution([403, 40]):15}{solution1([403, 40])}')


# def solution3(numbers):
#     numbers = list(map(str, numbers))
#     # 문자열 비교연산의 경우엔
#     # 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다.
#     # 물론 같으면, 다음 인덱스도 비교합니다
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))


# import functools
#
# def comparator(a,b):
#     t1 = a+b
#     t2 = b+a
#     return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0
#
# def solution(numbers):
#     n = [str(x) for x in numbers]
#     n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
#     answer = str(int(''.join(n)))
#     return answer

# import functools
# cmp_to_key
# 첫 번째가 두 번째보다
# 작으면(less-than) 음수 값을 반환하고,
# 같으면 0을 반환하고,
# 크면(greater-than) 양수 값을 반환해야 합니다.
#
# x-y값이 음수가 나오면, 정상적으로 진행해서 다음 요소 두개를 계산한다.
# x-y값이 양수가 나오면,  다른 요소와 비교해 정렬시킨다.



