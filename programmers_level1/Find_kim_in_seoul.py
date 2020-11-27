def solution(seoul):

    answer = seoul.index('Kim')

    return f'김서방은 {answer}에 있다'


def solution1(seoul):

    for i, v in enumerate(seoul):
        if v == 'Kim':
            return f'김서방은 {i}에 있다'


print(solution(['Jane', 'Kim']))
print(solution1(['Jane', 'Kim']))
