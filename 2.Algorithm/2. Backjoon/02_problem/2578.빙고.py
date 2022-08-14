# 2578 빙고
# 설계 의도:
# 1. 1차원 리스트를 2차원 배열처럼 쓰는 연습용도로 사용해봄
# 2. for문을 한번만 사용해서 2차원 탐색을 시도
board = [list(map(int, input().split())) for _ in range(5)]
board_25 = []                                      # 내 번호, 2차원으로 받은 걸
for i in range(5):
    board_25 += board[i]                           # 굳이 1차원으로 바꿔줌

call_list = [list(map(int, input().split())) for _ in range(5)]
call_25 = []                                       # 사회자 번호, 2차원으로 받은 걸
for j in range(5):
    call_25 += call_list[j]                        # 굳이 1차원으로 바꿔줌

check_board = [0]*12
# 앞의 5개는 가로, 뒤 5개는 세로, 대각선과 역대각선 카운팅을 위해 총 12개 제작

counting = 1                                       # 첫 시도는 카운팅 1부터 시작
for num_call in range(25):                         # 1차원 탐색이므로 5*5= 25개
    position = board_25.index(call_25[num_call])   # 바로 내 보드에서 숫자 찾아줌
    px = position // 5                             # px는 2차원 배열 상 list[i][0]
    py = position % 5                              # py는 2차원 배열 상 list[i][1]
    if px == py:                                   # 대각선 조건시 11번째 카운팅 +1
        check_board[10] += 1
    if px == 4 - py:                               # 역대각선도 동일하게 +1
        check_board[11] += 1
    check_board[5 + px] += 1                       # 기본적으로 좌표의 가로, 세로열
    check_board[py] += 1                           # 각각의 좌표값에 카운팅 +1
	# ex) 13이 [2,1] 위치에 있다면, 3행 값에 +1, 2열 값에 +1 해줘서 빙고 조건 카운팅
    if check_board.count(5) >= 3:                  # 5개, 즉 빙고 달성 3개 이상
        print(counting)                            # 시행 횟수 출력
        break
    else:
        counting += 1
