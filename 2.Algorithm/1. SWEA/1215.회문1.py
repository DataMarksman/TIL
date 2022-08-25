# 1215. 회문1
# 설계: 계속 앞뒤 챙겨야 하면, 그냥 재귀함수 만드는게 편하지 않나요...

T = 10
for case_num in range(1, T+1):
    N = int(input())
    ans_count = 0
    board = [list(input()) for _ in range(8)]
    re_board = list(map(list, zip(*board)))

    for dx in range(8):
        for dy in range(8-(N-1)):
            if board[dx][dy:dy+N] == board[dx][dy:dy+N][::-1]:
                ans_count += 1
            if re_board[dx][dy:dy+N] == re_board[dx][dy:dy+N][::-1]:
                ans_count += 1
    print(f'#{case_num} {ans_count}')
