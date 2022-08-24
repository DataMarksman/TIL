# SWEA. 14559. 배수 그래프
# 설계 목적:
# 0. 이전까지 했던거 ver1에 킵하고, 다른 방식으로 접근.
# 1. 쉽게 말해서, 각 길목들, 처음에 일괄적으로 매핑해버리자.
# 2. 갈 수 있는 곳 없는 곳 바로 체크해서 슥슥 그려버리면 되잖아?!
# 3. [시작점, 끝점] 리스트에서 각 리스트와의 연결 여부를 반환 및 저장하기!
# 4. 이렇게 저장하면 생기는 이점 2가지.
#   i) (백트1) 시작지점과 연결되는 정점이 없거나, 끝 점으로 가는 정점이 없으면 바로 -1 출력
#   ii) (백트2) 이후 방법론은 BFS와 동일하게 가져감. visited를 활용할 예정.
#           -> 한번 지나간 길은 지나가지 않음

def lining(root, visited, n):
    global ans_list

    if board[root][M] == 1:
        ans_list += [n]
    elif len(ans_list) > 0 and n > min(ans_list):
        return
    elif n >= M+2:
        return
    else:
        for check in range(M):
            if board[root][check] == 1 and check not in visited:
                visited.append(check)
                lining(check, visited, n+1)
                visited.remove(check)


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
    flag = False
    for first_check in range(M+1):
        if board[M][first_check] != 0 or board[first_check][M] != 0:
            flag = True
            break
    if flag:
        lining(M, [], 0)

    if flag is False or len(ans_list) == 0:
        print(f'#{case_num} {-1}')
    else:
        print(f'#{case_num} {min(ans_list)}')
