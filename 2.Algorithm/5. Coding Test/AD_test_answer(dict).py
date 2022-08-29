# 1. 전기자동차 충전소
# 설계 의도:
# 0.
# 1. 맨하탄 거리 기준으로 충전소를 설치함.
#    이 때 고려해야 할 부분은 최대 2개라는 점.
#   우선적으로 1개로 고려해야하므로, 첫루트는 1개 완전 탐색
# 2. 1개로 완전 탐색이 불가능할 경우,
#    set에 차이의 합을 저장하는 순열 조합으로 간다.

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    houses = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    max_set = set()
    station_list = []
    board = [[0]*31 for dk in range(31)]
    for put_in in range(N):
        houses[put_in][0] += 15
        houses[put_in][1] += 15
        px = houses[put_in][0]
        py = houses[put_in][1]
        pd = houses[put_in][2]
        for distance in range(pd + 1):
            if 0 <= px-pd+distance <= 30 and 0 <= py-distance <= 30 and 0 <= py+distance <= 30:
                board[px-pd+distance][py-distance:py+distance+1] += 1
        for distance in range(1, pd+1):
            if 0 <= px-pd+distance <= 30 and 0 <= py-distance <= 30 and 0 <= py+distance <= 30:
                board[px+distance][py-pd+distance:py+pd-distance+1] += 1

    for x in range(32):
        for y in range(32):
            if board[x][y] >= 1:
                station_list.append((board[x][y], (x, y)))
    station_list.sort(reverse=True)
    first_set = set()
    for first_check in range(len(station_list)):
        if station_list[first_check][0] == N:
            first_set.add








