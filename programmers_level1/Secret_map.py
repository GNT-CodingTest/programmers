def solution(n, arr1, arr2):
    answer = []

    for a1, a2 in zip(arr1, arr2):
        binary = bin(a1 | a2)[2:]

        temp = ''
        if len(binary) != n:
            temp += ' ' * (n - len(binary))
        for c in binary:
            if c == '1':
                temp += '#'
            else:
                temp += ' '

        answer.append(temp)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))

# for i,j in zip(arr1,arr2):
#     a12 = str(bin(i|j)[2:])
#       rjust 오른쪽 정렬 빈칸은 0으로
#     a12=a12.rjust(n,'0')
#     a12=a12.replace('1','#')
#     a12=a12.replace('0',' ')
#     answer.append(a12)

#  sub('x', 'X', 'strstr')
#  'strstr'에서 'x'가 있으면 'X'로 바꿔라
