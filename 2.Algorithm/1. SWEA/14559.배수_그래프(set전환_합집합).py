# SWEA. 14559. 배수 그래프
# 설계 목적:
# 0. 이전까지 했던거 일단 킵하고,
# 1. 쉽게 말해서, 교집합을 구하자.
# 2. 도착점으로 갈 수 있는 경로의 집합들을 구하고
# 3. (커팅1) 앞에서부터 나올 수 있는 모든 경로들을 set에 저장해서 뒤의 집합과 교집합 구하기
# 4. (백트1) n차 시도에서 실패시, 전열의 집합 내 모든 정점에서 갈 수 있는 정점을 다시 뽑아내고 돌리기
#   -> 이 때, 전열에서 갈 수 있는 정점을 다 뽑아낸 뒤에, 이전 정점들을 visited set에 저장.
#   -> 즉, 해당 정점을 밟고 2턴 뒤부터는 그 정점을 쓸 수 없게 된다.


T = int(input())
for case_num in range(1, T+1):
    N, S, E = map(int, input().split())
    N = int(N)
    start = int(S)
    end = int(E)

    ans_list = []

    M = int(input())
    board = [[0]*(M+1) for _ in range(M+1)]

    multiple_list = []
    for write_in in range(M):
        multiple_list += [list(map(int, input().split()))]

    for i in range(M):
        r = multiple_list[i][0]
        c = multiple_list[i][1]
        if start % r == 0:
            board[M][i] = 1
        if end % c == 0:
            board[i][M] = 1
        for j in range(M):
            if c % multiple_list[j][0] == 0 or multiple_list[j][0] % c == 0 or N >= c * multiple_list[j][0]:
                board[i][j] = 1
            if r % multiple_list[j][1] == 0 or multiple_list[j][1] % r == 0 or N >= r * multiple_list[j][1]:
                board[j][i] = 1

    first_set = set()
    last_set = set()
    for first_check in range(M+1):
        if board[M][first_check] == 1:
            first_set.add(first_check)
        if board[first_check][M] == 1:
            last_set.add(first_check)
    n = 0
    while n > M+1:
        if first_set & last_set


    if len(first_set)*len(last_set) == 0:
        print(f'#{case_num} {-1}')
    else:
        print(f'#{case_num} {min(ans_list)}')
