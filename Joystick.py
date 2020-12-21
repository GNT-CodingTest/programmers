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


print(solution('JEROEN'))
print(solution('JAN'))
print(solution('ABAAAAABAB'))
print(solution('ABABAAAAAB'))
#  => why 8?
