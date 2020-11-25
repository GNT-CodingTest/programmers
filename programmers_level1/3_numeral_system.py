def solution2(n):

    temp = []
    while n != 1:
        # n, r = (n/3, n%3)
        # n, r = divmod(n, 3)
        n, r = (n // 3, n % 3)
        temp.append(r)
    temp.append(n)

    answer = 0
    temp_len = len(temp)
    for i in range(temp_len):
        if temp[i] != 0:
            ans = temp[i] * 3 ** (temp_len - i - 1)
            answer += ans

    return answer


def solution3(n):
    temp = []
    while n > 2:
        temp.append(n % 3)
        n = n // 3
    temp.append(n)
    print(temp)

    answer = 0
    e = len(temp) - 1
    for i in range(len(temp)):
        if temp[i] != 0:
            answer += (temp[i] * 3 ** e)

        e -= 1

    return answer


def solution4(n):
    temp = []
    while n > 3:
        temp.append(n % 3)
        n = n // 3
    temp.append(n)
    print(temp)

    answer = 0
    e = len(temp) - 1
    for i in range(len(temp)):
        if temp[i] != 0:
            answer += (temp[i] * 3 ** e)

        e -= 1

    return answer


print(solution3(6234))
# print(solution4(6234))
print(solution3(9))
# print(solution4(9))

# answer.reverse()
# sum = 0
# for i in range(len(answer)):
#     sum += (answer[i] * (3 ** i))
# return sum


# a = ''
# while n>0:
#     a+=str(n%3)
#     n = n//3
