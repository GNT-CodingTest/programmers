def solution(x):

    temp = 0
    for c in str(x):
        temp += int(c)

    return not (x % temp)
# return not ( x % sum([int(c) for c in str(x)]))


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))
