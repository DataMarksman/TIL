# 2806. N-Queen
def queen_up(check, cross_check, r_cross_check, n):               # 재귀용 함수!
    global count                                                  # count 에 바로 반영해줄겁니다.
    if n >= N:                                                    # 반환할 조건은, n이 N에 도달했을 때
        count += 1                                                # 여기까지 도달하면 카운트 +1

    else:                                                         #
        for i in range(N):                                        # 백트래킹: 현재까지의 합이 첫 시도 아래인 경우!
            if check[i] == 0 and cross_check[n+i] == 0 and r_cross_check[N+(n-i)] == 0:
                check[i] = 1                                      # 앞서 밟았던 열, 대각선, 역대각선이 아니라면,
                cross_check[n+i] = 1                              # 내가 밟은 열, 대각선, 역대각선에 표시해주기
                r_cross_check[N+(n-i)] = 1
                queen_up(check, cross_check, r_cross_check, n+1)  # 재귀 함수에 n+1 해서 돌려줘!
                check[i] = 0                                      # 다시 열 밟은 흔적 지우고
                cross_check[n+i] = 0                              # 대각선 밟은 흔적 지우고
                r_cross_check[N+(n - i)] = 0                      # 역대각선 밟은 흔적 지우겠습니다~ 다음 루트 고고!


for case_num in range(1, int(input())+1):                         #
    N = int(input())                                              #
    count = 0                                                     #
    queen_up([0]*N, [0]*(2*N), [0]*(2*N), 0)                      # 함수에 (열 체크, 대각선, 역대각선, 0번 시도)넣기
    print(f'#{case_num} {count}')                                 # 출력

# 체스판을 봤을 때,
#    0     1     2     3     4     5     6
# 0(0,0)                  *(0,4)  -> 역대각선: 위치 좌표 (x,y)의 합 [x+y]가 일치하는 좌표를 의미.
# 1      (1,1)      *(1,3)
# 2           *(2,2)
# 3     *(1,3)-      (3,3)        -> 대각선: 위치 좌표 (x,y)의 차이, 즉 [x-y]가 일치하는 좌표를 의미.
# 4            (2,4)-
# 5                  (5,3)-       -> 대각선: 단, 위치 좌표중 y가 더 큰 경우,
# 6                                         x-y가 음수값이 나오므로, N+(x-y)로 양수화
