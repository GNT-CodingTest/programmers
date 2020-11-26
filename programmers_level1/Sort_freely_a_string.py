def solution(strings, n):
    answer = []

    dic = {}
    # for i in strings:
    #     if i[n:] in dic:
    #         dic[i[n:]].append(i)
    #     else:
    #         dic[i[n:]] = [i]

    for i in strings:
        if i[n:n+1] in dic:
            dic[i[n:n+1]].append(i)
        else:
            dic[i[n:n+1]] = [i]

    key = sorted(dic.keys())
    for k in sorted(key):
        val = dic[k]
        for v in sorted(val):
            answer.append(v)

    return answer


# [car, bed, sun]
print(solution(['sun', 'bed', 'car'], 1))

# [abcd, abce, cdx]
print(solution(['abce', 'abcd', 'cdx'], 2))

# [aacd, abcd, adcd]
print(solution(['abce', 'abcd', 'aacd'], 2))


# return sorted(strings, key=lambda x: x[n])
# 설명 https://stackoverflow.com/questions/13669252/what-is-key-lambda

# def sortkey(x):
#         return x[n]
# strings.sort(key=sortkey)

# sorted(dict.items(), key=operator.itemgetter(0))
# => sorted(dict.items())의 결과물의 0번째 아이템을 기준으로 정렬 => key값으로 정렬
# => value로 정렬하려면
# => sorted(dict.items(), key=operator.itemgetter(1))


