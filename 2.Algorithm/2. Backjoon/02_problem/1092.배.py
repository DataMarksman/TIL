# BOJ. 1092 배
# 설계 의도: 그리디
# 각 시행마다 최적의 횟수를 도출한다.
# 개선점:
# 어예 1등이당.

import sys
from math import ceil
input = sys.stdin.readline

# 크레인 받고, 내림차순 정렬 합니다. 뒤에서부터 빼올 겁니다.
N = int(input())
crane_list = sorted(list(map(int, input().split())), reverse=True)

# 화물 받고, 오름차순 정렬 합니다. 앞에서부터 나갈겁니다.
M = int(input())
freight_list = sorted(list(map(int, input().split())))

# 각 크레인이 몇개를 나르는지 파악하고, 최대값을 갱신해줄겁니다.
ans = 0
# ans_list = []
#  만약, 문제에서 최적의 상황일때, 가장 많이 나르는 친구랑 적게 나르는 친구 구하라고 하면,
#  이렇게 짜놓고 append 하면 됩니다.

# 나르지 못하는 경우는 -1로 바로 빼줍니다.
if max(freight_list) > max(crane_list):
    print(-1)
else:
    # 화물 선적 시작값은 0부터, 즉 가장 가벼운것부터 시작합니다.
    freight_top = 0

    # 크레인은 가장 약한 것 부터, 즉 N-1 의 위치에 있는 친구부터 시작합니다.
    while M > 0 and N > 0:
        # 이번 크레인이 옮겨야할 최적의 화물 수를 먼저 책정합니다.
        freight_add = ceil(M/N) - 1

        # 크레인이 작동했으니 남은 크레인 개수를 한개 줄여줍니다.
        N -= 1

        while True:
            # 최적의 개수가 있는 위치, 즉 이 크레인이 옮길 수 있는 최적의 위치까지의 박스 중
            # 가장 무거운 박르를 옮길 수 없다면, 하나씩 내려오면서 찾습니다.
            if freight_list[freight_top + freight_add] > crane_list[N]:
                freight_add -= 1
                if freight_add < 0:
                    break

            else:
                # 얘가 옮길 수 있는 가장 무거운 박스가 위치한 위치 정보를 기반으로 다음 시작점을 갱신해줍니다.
                freight_top += (freight_add + 1)

                # 남은 화물 수를 바꿔줍니다.
                M -= (freight_add + 1)

                # 이번에 옮긴 화물 개수가 가장 많다면, 답안을 바꿔줍니다.
                if freight_add > ans:
                    ans = freight_add
                break
    # 근데, 이 화물 운송은 idx 0 부터 시작하므로, 실제 크레인별 최다 화물 개수, 즉 걸린 시간은 + 1 해줘야 합니다.
    print(ans + 1)