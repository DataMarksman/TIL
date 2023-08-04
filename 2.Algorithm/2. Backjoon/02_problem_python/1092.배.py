<<<<<<< HEAD
# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
# crane_list = sorted(list(map(int, input().split())), reverse=True)
crane_list = list(map(int, input().split()))
crane_list.sort(reverse=True)

M = int(input())
# freight_list = sorted(list(map(int, input().split())), reverse=True)
freight_list = list(map(int, input().split()))
freight_list.sort(reverse=True)


if max(freight_list) > max(crane_list):
    print(-1)
else:
    # 아 모르겠슴다. 그리디로 한방에 풀 수 있을 것 같은데, 일단 노가다로 풀겠슴다
    time = 0
    while len(freight_list) > 0:
        for crane in crane_list:
            for weight in freight_list:
                if crane >= weight:
                    freight_list.remove(weight)
                    break
        time += 1
    print(time)

# else:
#     best_ans = M//N
#     if best_ans == 0:
#         best_ans = 1
#     if M%N != 0:
#         best_ans += 1
#
#     cut_list = []
#     top = 0
#     for box_check in range(M):
#         if freight_list[box_check] > crane_list[top]:
#             top += 1
#             cut_list.append(box_check+1)
#         if top == N-1:
#             cut_list.append(M)
#             break
#     point = 0
#     for check in range(len(cut_list)):
#         if cut_list[check] < best_ans*(check+1):
#             if point < cut_list[check] - best_ans*(check+1):
#                 point = cut_list[check] - best_ans*(check+1)
#     print(best_ans + point)



=======
# BOJ. 1092 배
# 설계 의도: 그리디
# 각 시행마다 최적의 횟수를 도출한다.
# 개선점:
# 어예 1등이당.

import sys
from math import ceil
input = sys.stdin.readline

# 크레인 받고, 내림차순 정렬 합니다. 뒤에서부터 빼올 겁니다.
N = int(input())
crane_list = sorted(list(map(int, input().split())), reverse=True)

# 화물 받고, 오름차순 정렬 합니다. 앞에서부터 나갈겁니다.
M = int(input())
freight_list = sorted(list(map(int, input().split())))

# 각 크레인이 몇개를 나르는지 파악하고, 최대값을 갱신해줄겁니다.
ans = 0
# ans_list = []
#  만약, 문제에서 최적의 상황일때, 가장 많이 나르는 친구랑 적게 나르는 친구 구하라고 하면,
#  이렇게 짜놓고 append 하면 됩니다.

# 나르지 못하는 경우는 -1로 바로 빼줍니다.
if max(freight_list) > max(crane_list):
    print(-1)
else:
    # 화물 선적 시작값은 0부터, 즉 가장 가벼운것부터 시작합니다.
    freight_top = 0

    # 크레인은 가장 약한 것 부터, 즉 N-1 의 위치에 있는 친구부터 시작합니다.
    while M > 0 and N > 0:
        # 이번 크레인이 옮겨야할 최적의 화물 수를 먼저 책정합니다.
        freight_add = ceil(M/N) - 1

        # 크레인이 작동했으니 남은 크레인 개수를 한개 줄여줍니다.
        N -= 1

        while True:
            # 최적의 개수가 있는 위치, 즉 이 크레인이 옮길 수 있는 최적의 위치까지의 박스 중
            # 가장 무거운 박르를 옮길 수 없다면, 하나씩 내려오면서 찾습니다.
            if freight_list[freight_top + freight_add] > crane_list[N]:
                freight_add -= 1
                if freight_add < 0:
                    break

            else:
                # 얘가 옮길 수 있는 가장 무거운 박스가 위치한 위치 정보를 기반으로 다음 시작점을 갱신해줍니다.
                freight_top += (freight_add + 1)

                # 남은 화물 수를 바꿔줍니다.
                M -= (freight_add + 1)

                # 이번에 옮긴 화물 개수가 가장 많다면, 답안을 바꿔줍니다.
                if freight_add > ans:
                    ans = freight_add
                break
    # 근데, 이 화물 운송은 idx 0 부터 시작하므로, 실제 크레인별 최다 화물 개수, 즉 걸린 시간은 + 1 해줘야 합니다.
    print(ans + 1)
>>>>>>> 87336fc2d248cdff1715e5f42ed7531a19b206ab
