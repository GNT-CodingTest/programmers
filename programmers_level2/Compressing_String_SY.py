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

        # print(f'step {step}: {compact_str} => len: {len(compact_str)}')

        if min_len > len(compact_str):
            min_len = len(compact_str)

    return min_len


# print(solution('aabbaccc'))
# print(solution('ababcdcdababcdcd'))
# print(solution('abcabcdede'))
# print(solution('abcabcabcabcdededededede'))
# print(solution('xababcdcdababcdcd'))
# print(solution('a'))


def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)


def solution2(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
    # for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)]:
    #     compress(text, tok_len)


print(solution2('aabbaccc'))
print(solution2('ababcdcdababcdcd'))
print(solution2('abcabcdede'))
print(solution2('abcabcabcabcdededededede'))
print(solution2('xababcdcdababcdcd'))
print(solution2('a'))
