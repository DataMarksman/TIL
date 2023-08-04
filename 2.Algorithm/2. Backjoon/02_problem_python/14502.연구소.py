# BOJ. 14502. 연구소
# 설계 의도: 조건에 맞는 실행
# 1. 최대 8 x 8 이므로 완전탐색 해보자.
# 2. 0으로 찍힌 곳을 position 리스트에 전부 넣고, 0의 개수를 카운팅한다.
# 3. 함수로 오염되는 곳을 카운팅해서 size에서 빼주고, 그 값을 set에 저장한다.
# 개선점:
# 조금 더 효율화 가능할 것 같은데 백트래킹 어떻게 하죠?

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def counting(A, B, C):
    shutter = set()
    shutter.add(tuple(position[A]))
    shutter.add(tuple(position[B]))
    shutter.add(tuple(position[C]))
    pol_count = 0
    visited = set()
    polluting_set = set(pollution)
    while polluting_set:
        point = polluting_set.pop()
        x = point[0]
        y = point[1]
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if 0 <= px < N and 0 <= py < M:
                if board[px][py] == 1 or (px, py) in shutter:
                    continue
                elif board[px][py] == 0 and (px, py) not in visited:
                    pol_count += 1
                    visited.add((px, py))
                    polluting_set.add((px, py))
    result = size - pol_count -3
    return result


N, M = tuple(map(int, input().split()))
board = []
position = []
pollution = []
for lining in range(N):
    line = list(map(int, input().split()))
    for checking in range(M):
        if line[checking] == 0:
            position.append((lining, checking))
        elif line[checking] == 2:
            pollution.append((lining, checking))
    board += [line]

size = len(position)
corruption = len(pollution)
ans_set = set()
for i in range(size-2):
    for j in range(i+1, size-1):
        for k in range(j+1, size):
            ans_set.add(counting(i, j, k))
print(max(ans_set))

