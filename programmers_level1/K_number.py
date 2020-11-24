def solution(array, commands):
    answer = []

    for command in commands:
        x = list(map(minus_1, command))

        temp = sorted(array[x[0]:x[1]+1])
        answer.append(temp[x[2]])

    return answer


def minus_1(a):
    return a - 1


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))


# return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
# list(
#   map(
#       lambda x :
#           sorted(array[x[0]-1 : x[1]]) => list
#           sorted(array[x[0]-1 : x[1]]) [x[2]-1]
#       , commands
#   )
# )

# for command in commands:
#   i,j,k = command
#   answer.append(-------)
