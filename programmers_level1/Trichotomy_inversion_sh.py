# 문제 설명
# 자연수 n이 매개변수로 주어집니다.
# n을 3진법 상에서 앞뒤로 뒤집은 후,
# 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# n은 1 이상 100,000,000 이하인 자연수입니다.
# 입출력 예
# n	    result
# 45	7
# 125	229

def solution(n):
    answer = 0
    trichotomy_answer = []

    for key in range(16, -1, -1):
        value = 3 ** key
        if n >= value:
            trichotomy_answer.append(n // value)
            n -= value * (n // value)
        if n == 0:
            trichotomy_answer.append(0)

    for key, value in enumerate(trichotomy_answer):
        answer += 3 ** key * value
    return answer


print(solution(6234))
print(solution(9))
print(solution(99999999))
