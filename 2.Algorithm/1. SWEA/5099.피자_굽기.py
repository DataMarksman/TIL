# SWEA. 5099 피자 굽기
# 설계 목적:
# 1.
# 개선점:
# 1.


T = int(input())
for case_num in range(1, T+1):
    N, M = tuple(map(int, input().split()))
    pizza_list = list(map(int, input().split()))
    pizza_queue = []
    pizza_number = 1
    ans = str()
    for pick in range(N):
        S = pizza_list.pop(0)
        pizza_queue.append((S, pizza_number))
        pizza_number += 1
    while pizza_queue:
        size = len(pizza_queue)
        for cooking in range(size):
            A, B = pizza_queue.pop(0)
            A = A//2
            if A == 0 and pizza_list:
                A = pizza_list.pop(0)
                B = pizza_number
                pizza_number += 1
                pizza_queue.append((A, B))
            elif A == 0 and not pizza_list:
                size -= 1
                if size == 0:
                    ans = B
                    pizza_queue.clear()
                    break
            else:
                pizza_queue.append((A, B))

    print(f'#{case_num} {ans}')
