def solution(s):
    answer = len(s)

    return s[answer//2] if answer%2 else s[(answer//2)-1:(answer//2)+1]
    # return str[(len(str)-1)//2:len(str)//2+1]


print(solution('abcde'))
print(solution('qwer'))
