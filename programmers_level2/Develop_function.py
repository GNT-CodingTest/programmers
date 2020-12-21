import collections as col


def solution(progresses, speeds):
    answer = []

    progresses = col.deque(progresses)
    speeds = col.deque(speeds)

    while progresses:
        # print(progresses)

        cnt = 0
        for i, v in enumerate(progresses):
            progresses[i] += speeds[i]

        while progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            cnt += 1

            if not progresses:
                break

        if cnt:
            answer.append(cnt)

    return answer


# print(solution([93, 30, 55], [1, 30, 5]))
# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))


def solution2(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        # 음수에서 정수 나누기는 내림 => 음수에서 내리면 절대값 커짐
        # 정수에서 정수 나누기는 버림
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


solution2([93, 30, 55], [1, 30, 5])
