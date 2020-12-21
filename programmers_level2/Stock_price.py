def solution(prices):
    answer = []
    queue = []

    pre = 0
    for idx, price in enumerate(prices):
        if not answer:
            answer.append(0)
            queue.append(idx)
            pre = price
        else:
            for q in queue:
                answer[q] += 1

            while pre > price:
                queue.pop()
                if queue:
                    pre = prices[queue[-1]]
                else:
                    break

            answer.append(0)
            queue.append(idx)
            pre = prices[queue[-1]]

    return answer


print(solution([1, 2, 3, 2, 3]))
print(solution([3, 4, 2, 6, 5]))
