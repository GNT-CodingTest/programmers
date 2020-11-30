# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.

# 입출력 예
# n	     return
# 12345	[5,4,3,2,1]


def solution(n):
    # 뒤에서 접근하려고 len(str(n))+1
    return [int(str(n)[-x]) for x in range(1, len(str(n))+1)]

# str(n) = '12345'
# str(n)[x] = '1', '2', '3', '4', '5'  -> if x from 0 to 4
# str(n)[-x] = '5', '4', '3', '2', '1' -> if x from 1 to 5
# int(str(n)[-x]) = 5, 4, 3, 2, 1
# [int(str(n)[-x])] = [5, 4, 3, 2, 1]

print(solution(12345))

print(list(map(int, reversed(str(12345)))))
