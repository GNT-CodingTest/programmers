def solution(n):
    big_array = [[0]*i for i in range(1, n+1)]

    _n = n
    step = 0
    num = 0
    while n > 0:
        edge = step*2
        for i in range(edge, edge+n):
            num += 1
            big_array[i][step] = num

        for i in range(step, step+n):
            big_array[edge+n-1][i] = num
            num += 1

        for i in range(_n-(2+step), edge, -1):
            big_array[i][-1 - step] = num
            num += 1

        n -= 3
        step += 1
        num -= 1

    answer = []
    for li in big_array:
        answer.extend(li)

    return answer


# print(solution(3))
# print(solution(4))
# print(solution(5))
print(solution(6))


def solution2(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    b = [[0]*i for i in range(1, n+1)]
    x, y = 0, 0
    num = 1
    d = 0

    while num <= (n+1) * n // 2:
        b[y][x] = num
        ny = y + dy[d]
        nx = x + dx[d]
        num += 1
        if (0 <= ny < n) and (0 <= nx <= ny) and (b[ny][nx] == 0):
            y, x = ny, nx
        else:
            d = (d+1) % 3
            y += dy[d]
            x += dx[d]

    return sum(b, [])


print(solution(6))
