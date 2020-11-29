def solution(arr1, arr2):
    answer = []

    for var1, var2 in zip(arr1, arr2):
        temp = []
        for x, y in zip(var1, var2):
            temp.append(x+y)
        answer.append(temp)

    return answer


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))
print(solution([[1], [2]], [[3], [4]]))

# answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]

# import numpy as np
# def sumMatrix(A,B):
#     A=np.array(A)
#     B=np.array(B)
#     answer=A+B
#     return answer.tolist()
