# 1216. 회문2
# 설계: 계속 앞뒤 챙겨야 하면, 그냥 재귀함수 만드는게 편하지 않나요...
def palindrome(platform, x, y_1, y_2, cnt):                          # 재귀용 함수
    global ans_list                                                  # 리스트 바로 수정하기.
    if y_1 < 0 or y_2 > 99:
        ans_list += [cnt]
    elif (platform[x][y_1] == platform[x][y_1+1]) and (y_1 == y_2):  # 첫 시도에서
        return palindrome(platform, x, y_1 - 1, y_2 + 2, 2)          # 짝수 펠린이면 2로 시작
    elif platform[x][y_1] == platform[x][y_2] and (y_1 == y_2):      # 첫 시도에서
        return palindrome(platform, x, y_1 - 1, y_2 + 1, 1)          # 홀수 펠린이면 1로 시작
    elif platform[x][y_1] == platform[x][y_2]:                       # 이후 펠린 지속되면
        return palindrome(platform, x, y_1 - 1, y_2 + 1, cnt + 2)    # 카운트 +2씩 계속
    else:
        ans_list += [cnt]


T = 10
for tc in range(1, T+1):
    case_num = int(input())
    ans_list = []
    board = [list(input()) for _ in range(100)]
    re_board = list(map(list, zip(*board)))
    for dx in range(100):
        for dy in range(99):
            palindrome(board, dx, dy, dy, 1)
            palindrome(re_board, dx, dy, dy, 1)
    print(f'#{case_num} {max(ans_list)}')