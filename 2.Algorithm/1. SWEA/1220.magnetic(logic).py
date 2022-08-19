# 1220. magnetic
# 이번 버전은 로직으로 푼 버전, 다른 버전은 직접 시뮬레이션 돌린 버전이다.
# 설계 의도: zip으로 돌리면 편하다. 안돌려도 구할 수는 있지만, 그냥 돌렸다.
# 1. N극 중 가장 위쪽에 위치한 아이의 좌표를 찾고, S극 중 가장 아래에 위치한 아이의 좌표를 찾는다.
# 2. On/off 버튼을 만들어서, N->S의 패턴이 끝날 때 마다 카운트를 한번씩 올린다.

# import sys
# sys.stdin = open("input_magnetic.txt", "r")

T = 10
for case_num in range(1, T+1):                                     #
    M = int(input())                                               #
    board = [list(map(int, input().split())) for _ in range(100)]  # 값을 받은 보드판 데이터를
    zip_board = list(map(list, zip(*board)))                       # 행으로 for 문 돌리기 위해 돌려준다.
    sum_count = 0                                                  #
    flag = False                                                   # On/off 스위치를 통해, 패턴의 개수 산출
    for x in range(100):                                           #
        start = zip_board[x].index(1)                              # 가장 먼저 나오는 N극 위치
        end = 99 - zip_board[x][::-1].index(2)                     # 가장 나중에 나오는 S극 위치
        for k in range(start, end+1):                              # 그 사이에서 구하면 나머지 떨거지 제외
            if zip_board[x][k] == 1 and flag is False:             # OFF 일 때, N극을 만나면
                flag = True                                        # 스위치 ON
            elif zip_board[x][k] == 2 and flag is True:            # ON 일 때, S극 만나면,
                sum_count += 1                                     # 패턴 1회 종료로 카운팅 +1 하고
                flag = False                                       # 스위치 OFF

    print(f'#{case_num} {sum_count}')                              #

