def solution(n):
    answer = ''
    temp = ['수', '박']
    for i in range(n):
        answer += temp[i%2]

    return answer


def solution2(n):
    s = "수박" * n
    return s[:n]
#   => ("수박" * n)[:n]


print(solution(3))
print(solution2(4))

# return "수박"*(n//2) + "수"*(n%2)

