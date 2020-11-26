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

def solution1(n):
    answer = 0
    trichotomy_answer = []
    test = False

    for key in range(16, -1, -1):
        value = 3 ** key
        if n >= value:
            if not test:
                test = True
            trichotomy_answer.append(n // value)
            n -= value * (n // value)
        elif n < value and test:
            trichotomy_answer.append(0)
        if n == 0:
            trichotomy_answer.append(0)
    for key, value in enumerate(trichotomy_answer):
        answer += (3 ** key) * value

    return answer


def solution2(n):
    answer = 0
    cnt = 1
    a = ''
    while n > 0:
        a += str(n % 3)  # a에 문자 n % 3 값을 넣어라
        n = n//3
    for b in range(len(a), 0, -1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer


def solution3(n):
    def convertBase(q, base):  # q: 9 / base: 3
        q, r = divmod(q, base)  # q: 3 / r: 0
        #      str(0)    q = 3  ->              3, 3 -> 0 + str(0)
        return str(r) if q == 0 else convertBase(q, base) + str(r)
    return int(convertBase(n, 3)[::-1], 3)  # '100' -> '001' int('001',3)

    # n=9 -> convertBase(n, 3) = 100
    # convertBase(n, 3)[::-1] -> 001
    # int('001',3) -> 1
    # int(문자열, 진법) return 10진수


print(solution1(6234))
print(solution2(9))
print(solution2(99999999))