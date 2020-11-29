def solution(num):
    answer = 0

    while num != 1:
        answer += 1

        if answer > 500:
            answer = -1
            break

        if num % 2:
            num = (num * 3) + 1
        else:
            num /= 2

    return answer


print(solution(6))
print(solution(16))
print(solution(626331))
