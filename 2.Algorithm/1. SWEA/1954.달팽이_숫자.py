# 1954. 달팽이 숫자
# 초반에 풀었던 알고리즘 다 날아간거 킹받네...
T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    board = [[0]*N for _ in range(N)]           # 숫자가 적힐 보드 제작 
    stock = 0                                   # 사이클 마다 축적된 sum
    for i in range(N//2):                       # 짝수는 딱 떨어지고 홀수는 1번 부족하게
        turn = ((N-1)-2*i)                      # turn = 사이클 변수
        for j in range(turn):                   # 매번 적기 힘들어서 넣음
            board[i][i+j] = stock + j+1                         # 시작점(1) [그림 설명]
            board[i+j][(N-1)-i] = stock + (turn)+(j+1)          # 시작점(2) [그림 설명]
            board[(N-1)-i][(N-1)-(i+j)] = stock + 2*(turn)+(j+1)# 시작점(3) [그림 설명]
            board[(N-1)-(i+j)][i] = stock + 3*(turn)+(j+1)      # 시작점(4) [그림 설명]
        stock += 4*(turn)                       # 사이클의 마지막 값을 다음 시작점에 더함
    if N % 2 == 1:                              # 홀수 N의 가운데 빵꾸에
        board[N//2][N//2] = N**2                # NxN 보드에 들어갈 마지막 값, N**2 기입
    print(f'#{case_num}')
    for lines in range(len(board)):             # 각 라인을 출력
        print(*board[lines])                    # 리스트 양 옆 [ ]를 언팩하기 위해 * 사용