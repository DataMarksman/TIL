# 1209. sum

T = 10                                       # 자꾸 오류나길래 확인해보니..
for tc in range(1,11):                       # 케이스 수 10으로 고정이었다니..
    case_num = int(input())                  # case_num도 직접 줍니다..
    board = [list(map(int,input().split()))\
            for _ in range(100)]             # 숫자가 적힌 보드 제작
    max_sum = 0
    for y in range(100):                     # 0~99까지 100회의 매핑 시전
        count_col = 0                        # 세로 합을 저장해놓을 스톡 및 초기화
        count_ver = 0                        # 가로 합을 저장해놓을 스톡 및 초기화
        for x in range(100):                 # x,y 좌표 돌아가려면 똑같이 100회
            count_col += board[x][y]         # 세로 합을 위해 앞 []가 변경됩니다.  
            count_ver += board[y][x]         # 가로 합을 위해 뒤 []가 변경됩니다.
            if count_col > max_sum:          # 현재 쌓인 세로합 스톡이 max 값보다 크면,
                max_sum = count_col          # 현재 세로합 스톡이 max값을 대체
            if count_ver > max_sum:          # 현재 쌓인 가로합 스톡이 max 값보다 크면,
                max_sum = count_ver          # 현재 가로합 스톡이 max값 대체
    count_cross = 0                          # 좌상 우하 대각선 스톡
    rv_count_cross = 0                       # 우상 좌하 대각선 스톡
    for z in range(100):                     # 똑같이 100회의 매핑 시전
        count_cross += board[z][z]           # x, y 값이 같아야 좌상 우하 대각선
        rv_count_cross += board[99-z][z]     # y 값이 99-x값과 같아야 우상 좌하 대각선
        if count_cross > max_sum:            # 똑같이 스톡 대체 여부 확인
                max_sum = count_cross
        if rv_count_cross > max_sum:
                max_sum = rv_count_cross
    print(f'#{case_num} {max_sum}')          # 출력
