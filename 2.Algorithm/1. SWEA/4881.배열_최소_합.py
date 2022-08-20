# 4881. 배열 최소 합

def sum_up(check, stock, n):                                # 재귀용 함수!
    global sum_list                                         # sum_list 에 합을 넣어줄 겁니다.
    if n >= N:                                              # 반환할 조건은, n이 N에 도달했을 때
        sum_list += [sum(stock)]                            # 지금까지 뽑아놓은 숫자의 합을 더한다.

    elif len(sum_list) <= 1 or sum(stock) < min(sum_list):  # <첫번째 시도> 거나,
        for i in range(N):                                  # 백트래킹: 현재까지의 합이 첫 시도 아래인 경우!
            if check[i] == 0:                               # 앞서 지나간 열이 아니라면,
                stock += [board[n][i]]                      # 현재 위치의 숫자를 뽑자
                check[i] = 1                                # 여기는 뽑은 열이라고 입력하고
                sum_up(check, stock, n+1)                   # 재귀 함수에 n+1 해서 돌려줘!
                check[i] = 0                                # 다시 열 밟은 흔적 지우고
                del stock[len(stock)-1]                     # 넣었던 숫자 다시 빼서 다음 발자국 밟으러 가!


for case_num in range(1, int(input())+1):                   #
    N = int(input())                                        #
    board = [[int(i) for i in input().split()] for _ in range(N)]
    sum_list = []                                           #
    sum_up([0]*N, [], 0)                                    # 함수에 (체크용 리스트, 빈 리스트, 0번 시도)넣기
    print(f'#{case_num} {min(sum_list)}')                   # 출력
