# 문제 설명
# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
#
# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.
# 입출력 예
# s	    return
# abcde	c
# qwer	we


# 100/100
def solution1(s):
    answer = ''

    if len(s) % 2 == 0:  # 짝수이면
        answer = "{0}{1}".format(s[int(len(s)/2 - 1)], s[int(len(s)/2)])
    else:                # 홀수이면
        answer = "{0}".format(s[int(len(s)/2)])

    return answer


# 100/100
def solution2(s):
    return "{0}{1}".format(s[int(len(s)/2 - 1)], s[int(len(s)/2)]) \
        if len(s) % 2 == 0 \
        else "{0}".format(s[int(len(s)/2)])


# 제일 짧은 방법
def solution3(s):  # 위의 솔루션과 비슷하지만 훨씬 간결함
    return s[(len(s)-1)//2:len(s)//2+1]  # 문자열 슬라이싱으로 범위를 지정하여 출력


print(solution1('가나다라마'))
print(solution1('pypy'))
print(solution2('가나다라마'))
print(solution2('pypy'))
print(solution3('가나다라마'))
print(solution3('pypy'))
