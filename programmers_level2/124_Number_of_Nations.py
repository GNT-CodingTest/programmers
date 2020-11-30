def solution(n):
    answer = ''

    while n != 0:
        temp = n % 3
        if temp:
            answer += str(temp)
        else:
            answer += '4'
            n -= 1

        n = n // 3

    return ''.join(reversed(answer))


for i in range(1, 20):
    print(solution(i))
