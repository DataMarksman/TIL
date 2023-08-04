# BOJ. 기차가.. 이하 생략
# 설계 의도: 비트 마스킹? 몰?루....
# 개선점:
# 비트 마스킹... 모르겠소요... 안쓰니까 336ms 나오네요. 쓰면 180대 나올지도
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
train_list = [['0']*20 for _ in range(N)]
for orders in range(M):
    order = list(map(int, input().split()))
    if len(order) == 2:
        idx = order[1] - 1
        if order[0] == 3:
            train_list[idx] = ['0'] + train_list[idx][:19]
        else:
            train_list[idx] = train_list[idx][1:] + ['0']
    elif len(order) == 3:
        idx = order[1] - 1
        sheet = order[2] - 1
        if order[0] == 1:
            train_list[idx][sheet] = '1'
        else:
            train_list[idx][sheet] = '0'
visited = set()
for making in range(N):
    visited.add(''.join(train_list[making]))
print(len(visited))
