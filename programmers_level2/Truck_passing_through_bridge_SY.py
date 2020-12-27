from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0

    truck_weights = list(reversed(truck_weights))
    trucks = len(truck_weights)

    queue = deque()
    cnt = 0
    while trucks != cnt:
        if queue:
            time = answer - queue[0][1]
            if time >= bridge_length:
                weight += queue[0][0]
                queue.popleft()
                cnt += 1

        if truck_weights and truck_weights[-1:] <= [weight]:
            queue.append([truck_weights.pop(), answer])
            weight -= queue[-1][0]

        answer += 1

    return answer


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
print(solution(5, 10, [7, 4, 5, 4, 6]))
