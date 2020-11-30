def solution(dart):
    answer = 0

    pre_c = ''
    pre_score = 11
    n_score = 0
    check = False
    for c in dart:
        temp = ord(c)
        if temp in range(48, 58):
            if check:
                answer += n_score
                pre_score = n_score

            if c == '0' and pre_c == '1':
                answer -= 1
                n_score = 10
            else:
                n_score = int(c)

        elif c in ('S', 'D', 'T'):
            if c == 'S':
                n_score = n_score ** 1
            elif c == 'D':
                n_score = n_score ** 2
            else:
                n_score = n_score ** 3

        else:
            if c == '*':
                if pre_score == 11:
                    n_score = n_score * 2
                else:
                    answer -= pre_score
                    answer += pre_score * 2
                    n_score = n_score * 2
            else:
                n_score = n_score * (-1)

        pre_c = c
        check = True

    answer += n_score

    return answer


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))

# 정규표현식(re)
# 메타문자 $()*+.?[\^{|
# \( => '('
import re


def solution1(dart_result):
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'': 1, '*': 2, '#': -1}

    # + => 1회 이상, * => 0회 이상, ? => 0번 또는 1번
    # 유니코드 (str) 패턴일 때: \d => [0-9]
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dart_result)
    # dart => [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]

    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer


solution1('1S2D*3T')

# point = ['10' if i == 'k' else i for i in dartResult]
