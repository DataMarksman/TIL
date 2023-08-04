# BOJ. 15685 드래곤 커브
# 설계 의도: 조건에 딱! 맞는 구현...
# 개선점:
# 1. 좌표 위의 x, y와 2차원 배열의 x,y를 잘 구별해야합니다.
# 2. 이 경우는 수학적인 좌표의 개념으로 가는 것과 이거저거 뒤섞어 놓은 상황입니다.
# 3. 그러면 간단합니다. 그냥 문제와 똑같이 구현하면 됩니다.
# 4. 오히려 제가 어느쪽으로 정할지 선택하는 것 보다 쉬울지도 모릅니다.

from copy import deepcopy
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

T = int(input())
dragon_set = set()
ans = 0
for writing in range(T):
    x, y, d, g = map(int, input().split())
    timer = 0
    dragon = [(x, y), (x + dx[d], y + dy[d]), ]
    while timer < g:
        timer += 1
        baby_dragon = deepcopy(dragon)
        R, C = baby_dragon.pop()
        while baby_dragon:
            X, Y = baby_dragon.pop()
            dragon.append((R + (C-Y), C - (R-X)))
    for drawing in range(len(dragon)):
        dragon_set.add(dragon[drawing])

check_set = deepcopy(dragon_set)
while check_set:
    DX, DY = check_set.pop()
    if (DX +1, DY) in dragon_set and (DX, DY-1) in dragon_set and (DX+1, DY-1) in dragon_set:
        ans += 1
print(ans)



