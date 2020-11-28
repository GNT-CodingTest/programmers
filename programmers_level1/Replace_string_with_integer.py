# 문제 설명
# 문자열 s를 숫자로 변환한 결과를 반환하는 함수, solution을 완성하세요.
#
# 제한 조건
# s의 길이는 1 이상 5이하입니다.
# s의 맨앞에는 부호(+, -)가 올 수 있습니다.
# s는 부호와 숫자로만 이루어져있습니다.
# s는 0으로 시작하지 않습니다.

# 입출력 예
# 예를들어 s가 '1234'이면 1234를 반환하고, '-1234'이면 -1234를 반환하면 됩니다.
# s는 부호(+,-)와 숫자로만 구성되어 있고, 잘못된 값이 입력되는 경우는 없습니다.


def solution(s):
    return int(s)


print(solution('1234'))
print(solution('-1234'))

#                       str[::-1]은 주어진 스트링을 거꾸로
# for idx, number in enumerate(str[::-1]):
#         if number == '-':
#             result *= -1
#         else:
#             각 자리에 10의 지수만큼 곱해서 더해줌
#             result += int(number) * (10 ** idx)
#
#     return result