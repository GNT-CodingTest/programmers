def solution(priorities, location):
    idx = priorities.index(max(priorities))
    _len = len(priorities[idx:])

    if location >= idx:
        location -= idx
    else:
        location += _len

    return location + 1


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
print(solution([1, 1, 9, 1, 1, 1], 2))
print(solution([1, 9, 1, 1, 9, 1], 2))

