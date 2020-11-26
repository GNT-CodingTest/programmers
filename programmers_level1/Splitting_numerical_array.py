def solution(arr, divisor):
    answer = []
    for i in arr:
        if not(i % divisor):
            answer.append(i)

    if not(len(answer)):
        answer.append(-1)

    return sorted(answer)


print(solution([5, 9, 7, 10], 5))
print(solution([2, 36, 1, 3], 1))
print(solution([3, 2, 6], 10))


# def solution(arr, divisor):
#   return sorted([n for n in arr if n%divisor == 0]) or [-1]
