def solution(n):
    answer = 0

    for i in range(1, n+1):
        if not(n%i):
            answer += i

    return answer


print(solution(12))
print(solution(5))

#       반 넘는 값은 검사할 필요 x
#     return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
#                                            => (num ** 0.5)+1 성능향상
#                                            => num / 2 성능향상


# return sum(filter(lambda x: num % x == 0, range(1, num + 1)))

# list comprehension
# sum([i for i in range(1,num+1) if num%i==0])
