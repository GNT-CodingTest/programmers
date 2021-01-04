def solution(number, k):

    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and num > stack[-1]:
            if k > 0:
                stack.pop()
                k -= 1
            else:
                break

        stack.append(num)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


print(solution('1924', 2))
print(solution('1231234', 3))
print(solution('4177252841', 4))
print(solution('12', 1))
print(solution('102', 2))
print(solution('989898', 3))
print(solution('87654321', 3))

