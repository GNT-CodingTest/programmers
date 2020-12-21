# 문제 설명
# 124 나라가 있습니다. 124 나라에서는 10진법이 아닌 다음과 같은 자신들만의 규칙으로 수를 표현합니다.
#
# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.
# 예를 들어서 124 나라에서 사용하는 숫자는 다음과 같이 변환됩니다.
#
# 10진법	124 나라
# 1	    1
# 2	    2
# 3	    4
# 4	    11
# 5	    12
# 6	    14
# 7	    21
# 8	    22
# 9	    24
# 10	41
# 11    42
# 12    44
# 13    111
# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.
#
# 제한사항
# n은 500,000,000이하의 자연수 입니다.

# 입출력 예
# n	result
# 1	1
# 2	2
# 3	4
# 4	11

def solution(n):
    nara = ['1', '2', '4']
    answer = ""

    while n:
        n -= 1
        answer = nara[n % 3] + answer
        n //= 3

    return answer


def change124(n):
    if n <= 3:
        return '124'[n-1]
    else:
        q, r = divmod(n-1, 3)
        return change124(q) + '124'[r]


print(solution(1))  # 1
print(solution(2))  # 2
print(solution(3))  # 4
print(solution(4))  # 4
print(solution(10))
print(solution(11))
print(solution(12))
print(solution(13))
