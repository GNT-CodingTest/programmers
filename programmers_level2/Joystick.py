def solution(name):
    answer = 0

    ascii_nums = []
    for c in name:
        ascii_nums.append(ord(c) - 65)

    idx = 0
    cnt = 0
    cal = 1
    while 1:
        if cnt >= len(name):
            break

        if ascii_nums[idx] > 13:
            answer += abs(ascii_nums[idx] - 26)
        else:
            answer += ascii_nums[idx]

        if cal != -1:
            temp = 0
            if ascii_nums[idx+1:idx+2] == [0]:
                for i in ascii_nums[idx+1:]:
                    if i == 0:
                        temp += 1
                    else:
                        break

                if temp > idx:
                    cal = -1
                    cnt += temp
                    answer += idx
                    idx = len(ascii_nums)

        idx += cal
        answer += 1
        cnt += 1

    return answer - 1


# print(solution('JEROEN'))
# print(solution('JAN'))
# print(solution('ABAAAAABAB'))
# print(solution('ABABAAAAAB'))
# ABABAAAAAB 미해결
# 이 문제 DFS나 다른 방법으로 풀어야 하고 레벨3짜리라고 봐야 합니다.


def solution2(name):
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = {}
    # 딕셔너리에 변경에 필요한 횟수 저장
    for i in range(len(alpha)):
        d[alpha[i]] = min(i, 26-i)
    print(d)

    indexes = []
    n = len(name)
    count = 0
    for i in range(n):
        num = d[name[i]]
        count += num
        if num != 0:
            # A가 아닌 문자들의 위치
            indexes.append(i)

    current_idx = 0
    while True:
        if len(indexes) == 0:
            break

        min_dist = 99
        min_idx = 0
        for it in indexes:
            # 현재 인덱스에서 다음 문자로 가는데
            # 오른쪽으로도 탐색, 왼쪽으로도 탐색 => 그중에 가까운거
            min_dist2 = min(abs(it-current_idx), n-abs(it-current_idx))

            # 현재 커서위치에서 몇번째에 인덱스를 먼저 처리할 것인가가?
            if min_dist2 < min_dist:
                min_dist = min_dist2
                min_idx = it

        count += min_dist
        indexes.remove(min_idx)
        current_idx = min_idx

    return count


solution2('ABAAAAABAB')
