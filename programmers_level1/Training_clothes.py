def solution(n, lost, reserve):
    have = [1] * n

    for i in lost:
        have[i-1] -= 1

    for i in reserve:
        have[i-1] += 1

    for i in range(len(have)):
        # 체육복이 없으면
        if have[i] == 0:
            # 없고 첫번째면
            if i == 0:
                # 오른쪽 아이가 가지고 있나?
                if have[i + 1] > 1:
                    have[i + 1] -= 1
                    have[i] += 1
            # 없고 마지막이면
            elif i == (len(have) - 1):
                # 왼쪽 아이가 가지고 있나?
                if have[i - 1] > 1:
                    have[i - 1] -= 1
                    have[i] += 1
            # 왼쪽 아이가 가지고 있으면
            elif have[i-1] > 1:
                have[i - 1] -= 1
                have[i] += 1
            # 오른쪽 아이가 가지고 있으면
            elif have[i+1] > 1:
                have[i + 1] -= 1
                have[i] += 1

    return len(have) - have.count(0)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(10, [1, 2, 3], [2, 4, 5, 8]))


'''
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
'''