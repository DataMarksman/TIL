# BOJ. 21610 마법사 상어와 비바라기
# 설계 의도: 2차원 값 받아서 돌면서 1차원 배열로 빼서 풀기.
# 1. 2차원 배열 받아서 1차원 배열로 뺀다.
# 2. 해당 배열에서 pop 하면, 규칙성이 보이기 때문에 훨씬 효율적이다.
# 3. 나머지는 그냥 빡구현

# 개선점: 빡구현 문제는 조건을 하나하나 잘 봐야한다. 각 항목별로 틀려서 3번 디버깅 함.
# 1. 블리자드로 터치는 건 점수에 안들어간다.
# 2. 연속된거 지울 때 는 한방에 싹 죽이고 다시 처음부터 돌면서 터쳐야 한다.
# 3. 다시 판 짤 때는 판 크기만큼 복붙해서 채우는 게 아니라, 그냥 있는거 가져다 붙이는 거다. 넘치는 것 만 커팅

# 4. python3 속도: 312ms, pypy 속도: 156ms (7등). 효율화 좀 더 해볼까...
import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
direction_dict = {1:3, 2:1, 3:0, 4:2}

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic_Q = []
ans = 0
X, Y = N//2, N//2

balls = (N*N)-1

# 탐색 하는 것. 우선순위 -> 현재 방향
# 진행 방향 좌측, 즉 회전의 안쪽에 0이 아닌 값이 있으면 해당 방향으로 꺾음.
D = 1
while True:
    for direct in [(D+3) % 4, D]:
        PX = X + dx[direct]
        PY = Y + dy[direct]
        if 0 <= PX < N and 0 <= PY < N:
            if board[PX][PY] != 0:
                D = direct
                magic_Q.append(board[PX][PY])
                board[PX][PY] = 0
                X = PX
                Y = PY
                break
    else:
        break

# 마법 방향, 거리 받을 때마다 시뮬레이션 실행
for turn in range(K):

    # 방향과 거리를 변수로 받기
    direction, length = map(int, input().split())
    direction = direction_dict[direction]

    # 좌: 0, 하: 1, 우: 2, 상: 3으로 값 재설정 해준 다음, 한발자국 씩 가면서 공식에 맞게 pop 하기.
    # 규칙성에서 나오듯이, 한바퀴 멀어질수록 2의 배수 만큼 중첩되도록 값이 커진다.
    # 해당 회전에서는 (2*depth) * 방향 만큼 증가하고, 이전에 쌓아놨던 (이전 depth*2)*4 이 기본값으로 배정된다.
    distance = 0
    for destroy in range(length):
        distance += 4*(2*destroy)
        if distance + direction*((destroy+1)*2) < len(magic_Q):
            magic_Q.pop(distance + direction*((destroy+1)*2))
        else:
            break

    # 4개 이상 연속 된 값이 있으면 그 값이 시작했던 temp_idx로 가서 연속된 개수만큼 pop 해준다.
    # 한바퀴 돌리면 다시 돌아가기. 해당 루틴에서 터진게 없으면 종료.
    flag = True
    while flag and magic_Q:
        value = -1
        count = 0
        temp_idx = 0
        idx = 0
        flag = False
        for checking in range(len(magic_Q)):
            if magic_Q[idx] != value:
                if count >= 4:
                    flag = True
                    for popping in range(count):
                        ans += magic_Q.pop(temp_idx)
                    idx = int(temp_idx)
                    value = magic_Q[idx]
                    count = 1
                    idx += 1
                else:
                    value = magic_Q[idx]
                    temp_idx = int(idx)
                    count = 1
                    idx += 1
            else:
                count += 1
                idx += 1
        if count >= 4:
            for popping in range(count):
                ans += magic_Q.pop()

    # 다음 배열을 만들기 위해서 New_Q 할당해주기.
    New_Q = []

    # 연속되는 숫자의 개수와 값을 새로운 배열에 넣어주기
    refill_count = 0
    refill_value = 0
    for filling in range(len(magic_Q)):
        if magic_Q[filling] != refill_value and refill_count > 0:
            New_Q.append(refill_count)
            New_Q.append(refill_value)
            refill_count = 1
            refill_value = magic_Q[filling]
        else:
            refill_count += 1
            refill_value = magic_Q[filling]
    if refill_count > 0:
        New_Q.append(refill_count)
        New_Q.append(refill_value)

    # 판 크기 이하의 길이만큼만 가져오기.
    magic_Q = New_Q[:balls]
print(ans)