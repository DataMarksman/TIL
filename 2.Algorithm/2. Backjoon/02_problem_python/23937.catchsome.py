# BOJ.
# 설계 의도:
# 자, N마리의 개 중에서 K 마리를 관잘해야한다고?
# 그러면 N 마리 전부 관찰하는 케이스에서 가장 멀리 있는 것들부터 빼야지!
# 1. 가장 멀리 있는 개가 속한 그룹(색상)을 뽑아내고, N-K 의 값이 그것보다 크면 해당 그룹은 제외.
# 2. 이런 방식으로 그룹들을 제외하다가 특정 그룹의 수준까지 내려오면 함수 시작.
# 3. 최대거리 함수가 작동하는 방식은 아래와 같다.
#       - 각 그룹에서 가장 먼 거리의 개의 위치를 구한다.
#       - 해당 위치의 값을 두배하여 모두 더해주고 가장 먼거리에 있는 것을 한번 빼준다. 끝.
# 4. 여기에서 중요한 점은 가장 멀리 있는 개가 속한 그룹이 중복되는 상태로 여러개 존재할때,
#   이렇게 중복된 그룹 중에서 그 다음 먼 거리에 있는 개가 있는 그룹을 우선적으로 빼야한다는 점이다.

# 개선점:
import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

T = int(input())
for case_num in range(1, T+1):
    N, K = map(int, input().split())
    distance = list(map(int, input().split()))
    color = list(map(int, input().split()))



    print(f'Case #{case_num}: {ans}')