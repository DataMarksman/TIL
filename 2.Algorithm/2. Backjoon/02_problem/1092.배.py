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



