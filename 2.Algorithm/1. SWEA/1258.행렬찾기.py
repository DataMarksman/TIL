# SWEA. 1258 행렬 찾기
# 설계 목적:
# 1. 0이 아닌 곳 탐색하면, 거기서부터 가로, 세로 범위로 0이 나오는 구간까지 진행 후,
#   해당 구간의 길이를 반환. 이를 저장하고 조건에 맞게 출력
# 개선점:
# 1. 프린트가 가장 어려웠다. 진짜로. 람다로 조건 주고 1차 정렬한 다음에 다시 엮어주고 단계별 프린트...

def find_mat(col, vert):
    global board
    global count
    cut_x = 0
    cut_y = 0
    for r in range(vert, N):
        if (board[col][r] == 0) or (r == (N-1)):
            cut_y = r
            break
    for c in range(col, N):
        if (board[c][vert] == 0) or (c == (N-1)):
            cut_x = c
            break
    for x in range(col, cut_x):
        for y in range(vert, cut_y):
            board[x][y] = 0

    ans = cut_x-col, cut_y-vert
    count += 1
    return ans


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    wide_list = []
    for dx in range(N):
        for dy in range(N):
            if board[dx][dy] != 0:
                wide_list += [find_mat(dx, dy)]
    ans_list = sorted(wide_list, key=lambda x: ((x[0]*x[1]), x[0], x[1]))
    r_ans = []
    for write_in in range(len(ans_list)):
        r_ans += ans_list[write_in]
    print(f'#{case_num} {count}', *r_ans)

