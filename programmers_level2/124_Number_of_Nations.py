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


def change124(n):
    num = ['1', '2', '4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


def change124(n):
    if n<=3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]
