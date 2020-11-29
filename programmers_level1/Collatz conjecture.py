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


# def collatz(num):
#     for i in range(500):
#         num = num / 2 if num % 2 == 0 else num*3 + 1
#         if num == 1:
#             return i + 1
#     return -1

# 재기호출도 가능
