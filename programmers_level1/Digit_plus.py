# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

def solution(n):
    answer = 0

    for c in str(n):
        answer += int(c)

    return answer


print(solution(123))
print(solution(987))


# if number < 10:
#   return number;
# return (number % 10) + sum_digit(number // 10)
#                           재귀 호출

# return sum(map(int,str(number)))
