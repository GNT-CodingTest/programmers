def solution(board, moves):
    answer = 0
    basket = []

    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                basket.append(board[i][move])
                board[i][move] = 0
                break

        if len(basket) > 1:
            if basket[-1] == basket[-2]:
                answer += 2
                del(basket[-2:])

    return answer


board1 = [[0, 0, 0, 0, 0],
          [0, 0, 1, 0, 3],
          [0, 2, 5, 0, 1],
          [4, 2, 4, 4, 2],
          [3, 5, 1, 3, 1]]

moves1 = [1, 5, 3, 5, 1, 2, 1, 4]

# board = [[0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [1, 0, 0, 0, 1]]
#
# moves = [1, 5, 3]

print(solution(board1, moves1))

# def solution(board, moves):
#     answer = 0
#
#     basket = []
#     for move in moves:
#         # board를 한줄씩
#         for line in board:
#             selectItem = line[move-1]
#             if(selectItem != 0):
#                 if (len(basket) > 0):
#                     if(basket[-1] == selectItem):
#                         # basket의 마지막 앞까지 => pop
#                         basket = basket[:-1]
#                         answer += 2
#                     else:
#                         basket.append(line[move-1])
#                 else:
#                     basket.append(line[move-1])
#
#                 line[move-1] = 0
#                 break
#
#     return answer

# def solution(board, moves):
#     stacklist = []
#     answer = 0
#
#     for i in moves:
#         for j in range(len(board)):
#             if board[j][i-1] != 0:
#                 stacklist.append(board[j][i-1])
#                 board[j][i-1] = 0
#
#                 if len(stacklist) > 1:
#                     if stacklist[-1] == stacklist[-2]:
#                         stacklist.pop()
#                         stacklist.pop()
#                         answer += 2
#                 break
#
#     return answer


a = [1, 2, 3]
print(a.pop())
