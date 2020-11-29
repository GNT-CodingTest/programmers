# 문제 설명
# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.

# 입출력 예
# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]

def solution1(n, m):
    answer = []
    max_nm = max(n, m)
    min_nm = min(n, m)

    for value in range(min_nm, 0, -1):
        if min_nm % value == 0 and max_nm % value == 0:
            answer.append(value)
            break

    for value in range(max_nm, (max_nm * min_nm) + 1, max_nm):
        # if value % min_nm == 0 and value % max_nm == 0:
        if value % min_nm == 0:
            answer.append(value)
            break
    return answer


def solution2(n, m):
    c, d = max(n, m), min(n, m)
    t = 1

    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(n * m / c)]

    return answer


# 제일 빠름
def solution3(n, m):
    gcd = lambda a, b: b if not a % b else gcd(b, a % b)
    lcm = lambda a, b: a*b//gcd(a, b)
    return [gcd(n, m), lcm(n, m)]


print(solution1(3, 12))
print(solution1(2, 5))

