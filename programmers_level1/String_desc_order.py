# 내림차순
# 대문자는 소문자보다 작은 것

def solution(s):
    return ''.join(sorted(s, reverse=True))


print(solution('Zbcdefg'))

# A => 65
# a => 97
# --------
# g => 103
# b => 98
# Z => 90
# 아스키 코드상으로 대문자가 이미 소문자보다 작음?!
