def solution(arr):

    del(arr[arr.index(min(arr))])

    return arr or [-1]


print(solution([4, 3, 2, 1]))
print(solution([10]))


# [i for i in mylist if i > min(mylist)]
