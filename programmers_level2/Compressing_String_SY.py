def solution(s):
    len_s = len(s)
    min_len = len_s
    for step in range(1, len_s//2 + 1):

        cnt = 0
        pre = ''
        compact_str = ''
        for idx in range(0, len_s, step):
            char = s[idx:idx+step]
            if pre == '':
                pre = char
                cnt = 1

            else:
                if pre == char:
                    cnt += 1

                else:
                    if cnt >= 2:
                        compact_str += str(cnt) + pre
                    else:
                        compact_str += pre

                    pre = char
                    cnt = 1

        else:
            if cnt >= 2:
                compact_str += str(cnt) + char
            else:
                compact_str += char

        print(f'step {step}: {compact_str} => len: {len(compact_str)}')

        if min_len > len(compact_str):
            min_len = len(compact_str)

    return min_len


print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
print(solution('a'))
