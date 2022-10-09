# SWEA. 5656. 벽돌 깨기
# 설계 목적: 재귀 + 90도 회전 후 각 열을 Q로 풀기 (연산 최적화)
# 0. 그냥 옆으로 돌리고 각 열을 Q로 보자.
# 1. 각 재귀마다 각 열의 끝 값을 뽑아서 큐에 올려놓고 돌린다.
# 2. 각 루틴마다 임시 보드를 만들어서 돌린다.

# < 루틴 >
# i) 큐에서 좌표 값을 하나 씩 뽑아옵니다.
# ii) 해당 좌표에 해당하는 값으로 상하좌우 체크 합니다.
# iii) 체크한 좌표들 중에 1 초과 값의 좌표는 큐에 넣고 나머지는 그냥 그 자리에서 임시 보드의 해당 좌표 값을 0으로 한다.
# iv) 큐를 전부 소진하면 루틴이 끝난다.

# 3. 루틴 종료 후, 0으로 바뀐 값들을 싹다 지워주고 다음 재귀로 진입한다.

# 개선점:
# 1. 현재 속도 964ms. 조금 더 커팅하면...
# 2. 맨탈이 나가서 for del_xy in range(pick[1] - value + 1, pick[1] + value): 에서
#     range 뒤의 값을 pick[1] + value -1 로 놓고 맞왜틀 하고 있었다.
from copy import deepcopy


def shoot_incur(k, re_board):
    global ans
    if ans != 0 and k < N:
        for shooting in range(wide):
            if re_board[shooting] and ans != 0:
                temp_board = deepcopy(re_board)
                queue = [(shooting, len(re_board[shooting])-1), ]
                while queue:
                    pick = queue.pop(0)
                    value = re_board[pick[0]][pick[1]]
                    temp_board[pick[0]][pick[1]] = 0
                    for del_x in range(pick[0] - value + 1, pick[0] + value):
                        if 0 <= del_x < wide:
                            if len(re_board[del_x]) > pick[1]:
                                if re_board[del_x][pick[1]] > 1 and temp_board[del_x][pick[1]] != 0:
                                    queue.append((del_x, pick[1]))
                                else:
                                    temp_board[del_x][pick[1]] = 0
                    for del_y in range(pick[1] - value + 1, pick[1] + value):
                        if 0 <= del_y < len(re_board[pick[0]]):
                            if re_board[pick[0]][del_y] > 1 and temp_board[pick[0]][del_y] != 0:
                                queue.append((pick[0], del_y))
                            else:
                                temp_board[pick[0]][del_y] = 0

                for shorting in range(wide):
                    if temp_board[shorting]:
                        while 0 in temp_board[shorting]:
                            temp_board[shorting].remove(0)
                if k <= N:
                    sum_count = 0
                    for summing in range(wide):
                        sum_count += len(temp_board[summing])
                    if sum_count < ans:
                        ans = sum_count
                    shoot_incur(k+1, temp_board)


T = int(input())
for case_num in range(1, T + 1):
    N, wide, height = map(int, input().split())
    input_board = [list(map(int, input().split())) for _ in range(height)]
    board = [[0]*height for _ in range(wide)]
    ans = 99999999999999
    for put_x in range(wide):
        for put_y in range(height):
            board[put_x][put_y] = input_board[height - put_y - 1][put_x]
        else:
            if 0 in board[put_x]:
                board[put_x] = board[put_x][:board[put_x].index(0)]
    shoot_incur(0, board)
    print(f'#{case_num} {ans}')
