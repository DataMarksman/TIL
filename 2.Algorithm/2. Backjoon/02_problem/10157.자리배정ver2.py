# BOJ. 10157 자리배정
# 설계 의도:
# 1. 이번에야말로 델타 탐색 가즈아~ 꼼수 안쓰고 정석대로 가즈아~
# 2. 스위치를 2개 배정! 한개는 방향 조타 스위치, 하나는 M, N turn 체크용
# 3. 이거 디버깅용으로 보드 있는 걸로 만들었슴다~
# 개선점:
# 1. 변수 N개 (N>1)를 받을 때, int 로 받되, map 처럼 휘발성 없게 받으려면?
# 2. M, N 나누지 않고 한방에 하는 방법은?

# 델타 탐색 조타용 변수
# 순서: 상 우 하 좌, %4 로 반복 예정
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = input().split()
N = int(N)
M = int(M)
K = int(input())
turn = 0
dir_turn = 0
now_idx = [M, 0]
check_MN = [[1, 0], [0, 1]]
# 쉽게 말해서, [[M 켜짐/꺼짐, M의 시행횟수], [N 켜짐/꺼짐, N의 시행횟수]]
board = [[0]*(N+1) for _ in range(M+1)]
flag = True
while (turn < M*N) and (flag is True):
    if check_MN[0][0] == 1:                       # 지금이 M, 즉 세로 와리가리하는 턴이니?
        for i in range(abs(M - check_MN[0][1])):       # 그러면, 이전 시행횟수 빼준 M값 만큼 반복문 돌려!
            turn += 1                             # turn + 1 해주고
            now_idx[0] += dx[dir_turn % 4]          # 위치 이동가즈아~
            now_idx[1] += dy[dir_turn % 4]
            board[now_idx[0]][now_idx[1]] = turn
            if turn == K:                         # K 값 나오면, 중간에 멈춰!
                ans = [now_idx[1] + 1, M - now_idx[0]]
                print(*ans)
                flag = False
                break
            # print(now_idx)
        check_MN[0][1] += 1                       # M 루트에 시행 횟수 + 1 해주자~
        # print(check_MN)

    elif check_MN[1][0] == 1:                     # 지금이 N, 즉 가로 와리가리하는 턴이니?
        for j in range(abs(N - check_MN[1][1])):       # 그러면, 이전 시행횟수 빼준 M값 만큼 반복문 돌려!
            turn += 1
            now_idx[0] += dx[dir_turn % 4]
            now_idx[1] += dy[dir_turn % 4]
            board[now_idx[0]][now_idx[1]] = turn
            if turn == K:
                ans = [now_idx[1] + 1, M - now_idx[0]]
                print(*ans)
                flag = False
                break
            # print(now_idx)
        check_MN[1][1] += 1
        # print(check_MN)
    dir_turn += 1                                 # 조타용 turn, + 1 해주고
    check_MN[0][0] = (check_MN[0][0]+1) % 2       # 스위치 끄기/켜기 전환
    check_MN[1][0] = (check_MN[1][0]+1) % 2       # 스위치 끄기/켜기 전환
    # print(f'한 사이클 끝난 뒤 turn: {turn}')
    # print(board)
if turn > M*N:
    print(int(0))

