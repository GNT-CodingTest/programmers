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
