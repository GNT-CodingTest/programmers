def solution(n):

    temp = []
    while n != 1:
        # q, r = (n/3, n%3)
        n, r = divmod(n, 3)
        temp.append(r)
    temp.append(n)

    answer = 0
    temp_len = len(temp)
    for i in range(temp_len):
        if temp[i] != 0:
            ans = temp[i] * 3**(temp_len - i - 1)
            answer += ans

    return answer


print(solution(45))
print(solution(125))
