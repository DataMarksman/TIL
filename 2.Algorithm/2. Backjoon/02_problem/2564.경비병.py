# BOJ.2564 경비병
# 설계 의도: 조건에 맞는 실행.. 각 패턴별 거리 도출 방법 차등 적용
# 개선점: 전부...
X, Y = map(int, input().split())
wide = int(X)
height = int(Y)

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]

my_idx = list(map(int, input().split()))
sum_stack = 0

for idx in range(N):
    len_x = num_list[idx][1] + my_idx[1]
    len_y = num_list[idx][1] - my_idx[1]
    # 동일 선상에 있는 패턴
    if num_list[idx][0] == my_idx[0]:
        sum_stack += abs(len_y)
    # 서로 반대편에 있는 패턴
    elif num_list[idx][0] + my_idx[0] == 7 or num_list[idx][0] + my_idx[0] == 3:
        if my_idx[0] < 3:
            sum_stack += height
            sum_stack += len_x if len_x < (2*wide-len_x) else (2*wide-len_x)
        else:
            sum_stack += wide
            sum_stack += len_x if len_x < (2 * height - len_x) else (2 * height - len_x)
    # 한칸 옆에 있는 패턴
    elif num_list[idx][0] + my_idx[0] == 4:
        sum_stack += len_x
    elif num_list[idx][0] + my_idx[0] == 6:
        sum_stack += height + wide - len_x
    elif num_list[idx][0] * my_idx[0] == 4:
        sum_stack += wide + len_y if my_idx[0] == 1 else wide - len_y
    elif num_list[idx][0] * my_idx[0] == 6:
        sum_stack += height + len_y if my_idx[0] == 3 else height - len_y
print(sum_stack)