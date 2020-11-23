from collections import deque
import time


def solution(bridge_length, weight, truck_weights):
    start = time.time()

    b_ing = [0 for i in range(bridge_length)]
    truck_weights = deque(truck_weights)

    sec = 0
    hap = 0
    is_true = True

    # len(truck_weights) * bridge_length
    while(1):
        if not truck_weights and hap == 0:
            print(f"걸린시간 :{time.time() - start:.10f}")
            return sec

        else:
            # 대기 트럭이 있다면
            if truck_weights:
                if b_ing[-1]:
                    # 1     1 => 2
                    hap -= b_ing[-1]
                    # 1 => 1
                    b_ing[-1] = 0

                # 트럭 이동
                if hap > 0:
                    # 약 bridge_length
                    # 약 10,000
                    for i in range(bridge_length-2, -1, -1):
                        b_ing[i + 1] = b_ing[i]

                    b_ing[0] = 0

                # 중량 초가?
                if hap + truck_weights[0] <= weight:
                    hap += truck_weights[0]
                    b_ing[0] = truck_weights.popleft()

            # 대기 트럭이 없다면
            else:
                if is_true:
                    print(f"중간시간 :{time.time() - start:.10f}")
                    is_true = False

                # 트럭 빼기
                if b_ing[-1]:
                    hap -= b_ing[-1]
                    b_ing[bridge_length - 1] = 0

                # 트럭 이동
                if hap > 0:
                    # 약 bridge_length
                    # 약 10,000
                    for i in range(bridge_length-2, -1, -1):
                        b_ing[i + 1] = b_ing[i]
                    b_ing[0] = 0

            sec += 1


def solution2(bridge_length, weight, truck_weights):
    start = time.time()

    b_ing = deque([0 for i in range(bridge_length)], maxlen=bridge_length)
    truck_weights = deque(truck_weights)

    sec = 0
    hap = 0
    is_true = True

    # len(truck_weights) * bridge_length
    # 5 * 10,000 => 50,001
    while (1):
        if not truck_weights and hap == 0:
            print(f"걸린시간 :{time.time() - start:.10f}")
            return sec

        else:
            # 대기 트럭이 있다면
            if truck_weights:
                if b_ing:
                    # 마지막 트럭 제거
                    # 1     1 => 2
                    hap -= b_ing.pop()

                # 중량 초가?
                if hap + truck_weights[0] <= weight:
                    # 1     1 => 2
                    hap += truck_weights[0]
                    # 1                 1   => 2
                    b_ing.appendleft(truck_weights.popleft())
                else:
                    # 1 => 1
                    b_ing.appendleft(0)

            # 대기 트럭이 없다면
            else:
                if is_true:
                    print(f"중간시간 :{time.time() - start:.10f}")
                    is_true = False

                if b_ing:
                    # 1     1 => 2?
                    hap -= b_ing.pop()

        # 약 8
        sec += 1


def solution3(bridge_length, weight, truck_weights):
    start = time.time()

    b_ing = [0 for i in range(bridge_length)]
    truck_weights = deque(truck_weights)

    sec = 0
    hap = 0
    is_true = True

    # len(truck_weights) * bridge_length
    while(1):
        if not truck_weights and hap == 0:
            print(f"걸린시간 :{time.time() - start:.10f}")
            return sec

        else:
            # 대기 트럭이 있다면
            if truck_weights:
                if b_ing[-1]:
                    # 1     1 => 2
                    hap -= b_ing[-1]
                    # 1 => 1
                    b_ing[-1] = 0

                # 중량 초가?
                if hap + truck_weights[0] <= weight:
                    for i in range(bridge_length-2, -1, -1):
                        b_ing[i + 1] = b_ing[i]

                    b_ing[0] = 0

                    hap += truck_weights[0]
                    b_ing[0] = truck_weights.popleft()
                else:
                    index = 0
                    for i in range(bridge_length - 2, -1, -1):
                        if b_ing[i] != 0:
                            index = i
                            break
                    hap -= b_ing[index]
                    del(b_ing[index:])
                    temp = b_ing[:index]
                    b_ing = ([0] * (bridge_length - index)) + temp

                    sec += bridge_length - index
                    continue

            # 대기 트럭이 없다면
            else:
                if is_true:
                    print(f"중간시간 :{time.time() - start:.10f}")
                    is_true = False

                # 트럭 빼기
                index = 0
                for i in range(bridge_length - 2, -1, -1):
                    if b_ing[i] != 0:
                        index = i
                        break
                hap -= b_ing[index]
                del (b_ing[index:])

                sec += bridge_length - index
                continue

        sec += 1


# print(solution(2, 10, [7, 4, 5, 6]))
# print(solution(100, 100, [10]))
# print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
#
# print('\n')
#
# print(solution2(2, 10, [7, 4, 5, 6]))
# print(solution2(100, 100, [10]))
# print(solution2(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))

# print(solution(10000, 10000, [10000, 10000, 10000, 10000, 10000]))
# # 중간시간 :40.1468279362
# # 걸린시간 :50.4100458622
# print('\n')
#
#
# print(solution2(10000, 10000, [10000, 10000, 10000, 10000, 10000]))
# # 중간시간 :0.0156216621
# # 걸린시간 :0.0156216621

print(solution3(2, 10, [7, 4, 5, 6]))
# print(solution3(10000, 10000, [10000, 10000, 10000, 10000, 10000]))
