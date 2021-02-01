def solution(scoville, K):
    answer = 0

    scoville.sort(reverse=True)
    print(scoville)

    while 1:
        one = scoville.pop()

        if one >= K:
            scoville.append(one)
            break
        else:
            two = scoville.pop()

            temp = one + (two * 2)
            scoville.append(temp)

            answer += 1

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
