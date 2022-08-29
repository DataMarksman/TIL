# 1. 전기자동차 충전소
# 설계 의도:
# 0.
# 1. 맨하탄 거리 기준으로 충전소를 설치함.
#    이 때 고려해야 할 부분은 최대 2개라는 점.
#   우선적으로 1개로 고려해야하므로, 첫루트는 1개 완전 탐색
# 2. 1개로 완전 탐색이 불가능할 경우,
#    set에 차이의 합을 저장하는 순열 조합으로 간다.
def lining():
    if core_



T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    board = []
    core_queue = []
    for put_in in range(N):
        line = list(map(int, input().split()))
        for check in range(N):
            if line[check] == 1:
                if check == 0 or check == N-1 or line == 0 or line == N-1:
                    line[check] = 2
                else:
                    core_queue.append((put_in, check))
        board += [line]










