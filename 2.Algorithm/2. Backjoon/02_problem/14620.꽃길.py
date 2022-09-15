# BOJ.14620 꽃길
# 설계 의도: 델타 탐색
# 1. 씨앗을 심을 수 있는 범위는 각 X, Y 축의 idx 1 ~ N-2의 범위까지이다.
# 2. 해당 범위를 전부 커버할 수 있는 모든 좌표를 location 리스트에 넣어준다.
# 3. 그 중에서 3개를 뽑아서 함수를 돌려준다.
# 4. < 함수 구동 >
#    i) 3개 뽑은 리스트에서 하나를 뽑아서, 델타 4방 탐색으로 밟는 5곳을 visited 에 저장.
#    ii) 나머지 2개도 동일하게 진행하면서 5군데 좌표가 visited 에 없으면 진행
#    iii) 단, 이때 중간에 visited 에 있는 곳을 밟거나, 이미 쌓인 price 가 min 값을 넘었으면 함수 정지
#    iv) 3개 전부다 5곳 전부 찍었으면 그 합계와 min 값을 비교하여 갱신.
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def flowering(pot_set):
    global min_price
    visited = set()
    price = 0
    count = 0
    while pot_set:
        pots = pot_set.pop()
        x = location[pots][0]
        y = location[pots][1]
        price += board[x][y]
        visited.add((x, y))
        for direction in range(4):
            px = x + dx[direction]
            py = y + dy[direction]
            if (px, py) not in visited:
                visited.add((px, py))
                price += board[px][py]
                if price > min_price:
                    pot_set = []
                    break
            else:
                pot_set = []
                break
        else:
            count += 1
    if count == 3:
        if price < min_price:
            min_price = int(price)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
min_price = 999999999
location = []
for x in range(1, N-1):
    for y in range(1, N-1):
        location.append([x, y])
for i in range(len(location)-2):
    for j in range(i+1, len(location)-1):
        for k in range(j+1, len(location)):
            flowering([i, j, k])
print(min_price)
