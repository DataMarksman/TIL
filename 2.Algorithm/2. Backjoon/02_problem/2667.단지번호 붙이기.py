# BOJ.2667 단지 번호 붙이기
# 설계 의도: 이미 밟았던 곳인가? 의 여부를 체크할 서브 보드를 만들자.
# 1. 사방 탐색으로 이어져있는 구간 구할거니까 조타용 dx dy 만들고, 탐색용 재귀함수 만들자.
# 2. 재귀 함수는 스택 올리고 앞에서부터 빼서 지나가주자.
# 3. 탐색할때 미리 서브 보드에 현재 깊이(n)를 기입해주고 해당 좌표 이동 후 다시 사방 탐색하면서 n 찍어주자.
# 4. 찍어주는건 visited 탐색용이고, 본체는 count. 각 깊이별 count 맞춰서 count_list에 기입해주자.
# 5. (빼먹었음) 출력시 오름차순. 현재 카운트와, 리스트 [1:]을 오름차순으로 출력해주면 된다.
# 개선점: 아.. 출력 조건도 같이 써주면서 하자구....

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def lining(stack, ex, ey, n):
    global re_board
    global num_count
    for dirt in range(4):
        if ori_board[ex+dx[dirt]][ey+dy[dirt]] == 1 and re_board[ex+dx[dirt]][ey+dy[dirt]] == 0:
            re_board[ex+dx[dirt]][ey+dy[dirt]] = n
            num_count[n] += 1
            stack.append([ex+dx[dirt], ey+dy[dirt]])
    if stack:
        next_po = stack.pop(0)
        lining(stack, next_po[0], next_po[1], n)


N = int(input())
ori_board = [[0]*(N+2)] + [[0] + list(map(int, input())) + [0] for _ in range(N)] + [[0]*(N+2)]
re_board = [[0]*(N+2) for _ in range(N+2)]
num_count = [0]
count = 0
for x in range(1, N+1):
    for y in range(1, N+1):
        if ori_board[x][y] == 1 and re_board[x][y] == 0:
            re_board[x][y] = 1
            count += 1
            num_count += [1]
            lining([], x, y, count)
num_count = sorted(num_count[1:])

print(count)
for print_nums in range(count):
    print(num_count[print_nums])


