def solution(a, b):
    # return sum(list(range(min(a, b), max(a, b)+1)))
    return sum(range(min(a, b), max(a, b)+1))


print(solution(3, 5))
print(solution(3, 3))
print(solution(5, 3))

# if a > b: a, b = b, a
#
# return sum(range(a,b+1))


# return (abs(a-b)+1)*(a+b)//2
#       abs(3-5)+1 => 3
#       3 * (3+5) => 24
#       24 // 2 => 12
