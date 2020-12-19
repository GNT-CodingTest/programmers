import collections as col


def solution(priorities, location):
    priorities = list(map(lambda x: [x, 0], priorities))
    priorities[location][1] = 1

    # print(priorities.index(max(priorities)))
    # temp = col.deque()
    cnt = 1
    while priorities:
        temp = col.deque()

        idx = priorities.index(max(priorities, key=lambda x: x[0]))
        temp.extend(priorities[idx:])
        temp.extend(priorities[:idx])

        ok = temp.popleft()
        if ok[1] == 1:
            return cnt
        else:
            cnt += 1
            priorities = list(temp)


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1, 1, 9, 1, 1, 1], 2))
print(solution([1, 9, 1, 9, 1], 2))


def solution2(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer


print(solution2([2, 1, 3, 2], 2))
print(solution2([1, 1, 9, 1, 1, 1], 0))
print(solution2([1, 1, 9, 1, 1, 1], 2))
print(solution2([1, 9, 1, 9, 1], 2))
