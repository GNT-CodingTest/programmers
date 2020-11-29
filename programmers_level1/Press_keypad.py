# 순서대로 누를 번호가 담긴 배열 numbers
# 손잡이인지 오른손잡이인 지를 나타내는 문자열 hand
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return

def solution(numbers, hand):
    answer = ''

    R = [3, 2]
    L = [3, 0]

    for num in numbers:
        if num == 0:
            taget = [3, 1]
        else:
            taget = [(num-1) // 3, (num-1) % 3]

        if num in (1, 4, 7, '*'):
            answer += 'L'
            L = taget

        elif num in (3, 6, 9, '#'):
            answer += 'R'
            R = taget

        else:
            r_dis = abs(R[0]-taget[0]) + abs(R[1]-taget[1])
            l_dis = abs(L[0]-taget[0]) + abs(L[1]-taget[1])

            if r_dis < l_dis:
                answer += 'R'
                R = taget
            elif r_dis > l_dis:
                answer += 'L'
                L = taget
            else:
                if hand == 'right':
                    answer += 'R'
                    R = taget
                else:
                    answer += 'L'
                    L = taget

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print('LRLLLRLLRRL')
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print('LRLLRRLLLRR')
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
print('LLRLLRLLRL')

print(solution([0], 'right'))
print(solution([0, 7, 5, 0], 'left'))

