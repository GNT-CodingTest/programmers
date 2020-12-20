def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:

        idx = 0
        for s_tree in skill_tree:
            if s_tree in skill:
                if s_tree == skill[idx]:
                    idx += 1
                else:
                    break
        else:
            answer += 1

    return answer


print(solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA']))


# 일단 다 넣고 마지막에 비교
# def solution(skill,skill_tree):
#     answer=0
#     for i in skill_tree:
#         skillist=''
#         for z in i:
#             if z in skill:
#                 skillist+=z
#         if skillist==skill[0:len(skillist)]:
#             answer+=1
#     return answer
