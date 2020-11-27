# 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화

def solution(s, n):
    answer = ''
    for c in s:
        if c.isalpha():
            temp = ord(c) + n
            if c.islower():
                if temp > 122:
                    answer += chr(temp - 26)
                else:
                    answer += chr(temp)
            else:
                if temp > 90:
                    answer += chr(temp - 26)
                else:
                    answer += chr(temp)
        else:
            answer += c

    return answer


print(solution('AB', 1))
print(solution('z', 1))
print(solution('a B z', 25))

# s = list(s)
# for i in range(len(s)):
#     if s[i].isupper():
#         s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
#     elif s[i].islower():
#         s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))
#
# return "".join(s)

# lower_list = "abcdefghijklmnopqrstuvwxyz"
# upper_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# result = []
#
# for i in s:
#     if i is " ":
#         result.append(" ")
#     elif i.islower() is True:
#         new_ = lower_list.find(i) + n
#         result.append(lower_list[new_ % 26])
#     else:
#         new_ = upper_list.find(i) + n
#         result.append(upper_list[new_ % 26])
# return "".join(result)

