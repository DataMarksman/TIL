# BOJ.
# 설계 의도: 각 턴마다 가장 많이 잡을 수 있는 케이스들을 쭉쭉 뽑자.
# 1. shooting 함수를 통해 해당 턴에서 해당 범위 내 잡을 수 있는 가장 많은 수를 도출한다.
# 2. 매 BFS를 시행할 때마다
#   각 궁수들에게서 매 행의 적들과의 길이를 도출하여, 해당 적들을 처단.
#   우선순위는 각 행의 모든 적을 죽이는 것이 최우선. 그 다음이
# 3. 각 궁수들의 위치는 순열로 모두 도출하여 위의 루틴에 집어 넣는다.
#   N은 최대 턴수로서, 가장 아래부터 d 만큼의 범위를 탐색하면서 올라오는 재귀함수를 만들어 사용해보자
#   .
# 개선점:
def shooting(depth, distance, batch, kill_sum):
    global board
    n = int(depth)
    d = int(distance)
    kill_count = [0, 0, 0]
    while sum(kill_count) < 3 and d > 0 and n >= 0:
        d -= 1
        for killing in range(M):
            if kill_count[0] == 0 and board[n][killing] == 1:
                if killing in range(batch[0]-d, batch[0]+d+1):
                    board[n][killing] = 0
                    kill_count[0] = 1
        for killing in range(M):
            if kill_count[1] == 0 and board[n][killing] == 1:
                if killing in range(batch[1]-d, batch[1]+d+1):
                    board[n][killing] = 0
                    kill_count[1] = 1
        for killing in range(M):
            if kill_count[2] == 0 and board[n][killing] == 1:
                if killing in range(batch[2]-d, batch[2]+d+1):
                    board[n][killing] = 0
                    kill_count[2] = 1
            if sum(kill_count) >= 3:
                d = 0
                break
        n -= 1
    kill_sum += sum(kill_count)
    if depth <= 0 or distance <= 0:
        return kill_sum
    elif depth - distance == 0:
        return shooting(depth - 1, distance - 1, batch, kill_sum)
    else:
        return shooting(depth - 1, distance, batch, kill_sum)


N, M, D = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
start = [0, 1, 2]
batch_set = set()
batch_position = [i for i in range(M)]
kill_count_set = set()
for i in range(M):
    for j in range(M):
        for k in range(M):
            if i < j < k:
                batch_set.add((i, j, k))
while batch_set:
    pick = batch_set.pop()
    kill_count_set.add(shooting(N-1, D, pick, 0))
print(max(kill_count_set))


