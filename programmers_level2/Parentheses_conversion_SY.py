def solution(p):
    answer = divide(p)

    return answer


def divide(s):
    if not s:
        return ''

    u = ''
    v = ''
    stay = ''
    status = 0
    for c in s:
        if c == '(':
            status += 1
            stay += c
        else:
            status -= 1
            stay += c

        if status == 0:
            if u == '':
                u += stay
            else:
                v += stay
            stay = ''

    dummy = 0

    if checking(u):
        return u + divide(v)
    else:
        return '(' + divide(v) + ')' + ''.join(list(map(lambda x: '(' if x != '(' else ')', u[1:-1])))


def checking(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False

    return True


print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))
# print(solution(')()()()('))
# print(solution(')))(()))(((('))
