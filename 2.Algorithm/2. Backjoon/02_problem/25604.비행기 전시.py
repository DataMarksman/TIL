# BOJ.
# 설계 의도:
# [파기] [0]*(math.ceil(10000/T)) 로 만들어서 최적화 하자 -> 중간에라도 운송 가능하면 해야함. 파기.
# [파기]
# 1. 단, 부품이 분해된 경우 출발 시간은 분해된 부품이 최초로 출발한 시간, 도착시간은 분해된 부품들이 모두 반대편에 완전히 도착했을 때의 시간이다.
# 개선점:
"""
조건들을 전부 나열해서 슈도 코드로 바꿔보자.

< 이 부분은 조건 제시 >
항공대에는 두 대의 비행기가 전시되어 있다.
현재 두 비행기는 각각 $0$번과 $1$번 위치에 전시되어 있다.
그리고 트럭이 한 비행기가 전시된 위치에서 다른 비행기가 전시된 위치로 가는데는 $T$의 시간이 소요된다.
항공대는 미관상의 이유로 두 비행기가 전시된 위치를 서로 바꾸려고 한다.
비행기는 매우 크기 때문에, 비행기를 옮기기 위해서는 비행기를 작은 부품들로 분해한 뒤 이를 재조립하는 방식을 사용한다.
양쪽 비행기에서 분해해 옮겨야 할 부품의 개수는 총 $N$개이며,
각 부품은 운송이 준비되는 순서대로 번호가 매겨진다.
그리고 부품을 옮기기 위한 트럭의 최대 적재량은 $M$이다.

1. 0 번과 1 번 큐 두개 운용, 그 두개의 요소 개수 합이 N
2. 이동에 T 시간 소요 -> 한번 루틴 돌면 T 소모

    while True:
        flag == 0 번 전시장 or 1 번 전시장

3. 트럭의 capacity == M
4. 트럭 자리 남으면 다음것도 케어 해야함

5. 이동시 capacity 만큼 전부 싣고 간다.
6.
        if queue[flag][0] > present:
            if queue[flag][0] >= queue[(flag+1)%2][0]:
                present += queue[flag][0] - present
            elif: T < queue[flag][0] - present:
                flag = (flag + 1)%2


반대편 비행기에 트럭이 도착할 경우, 트럭이 실은 부품을 모두 비운 후 트럭의 도착 시점에 운송이 준비된 부품들을 번호 순서대로 싣는다.
이때 부품을 싣고 내리는 시간은 고려하지 않는다. 준비된 부품을 최대한 실었다면 반대편으로 출발한다.

두 비행기에서 분해된 부품이 아직 운송이 준비되지 않은 경우도 존재할 수 있다.
이런 경우 하나의 부품이 준비될 때까지 기다리다가 부품이 먼저 준비된 쪽으로 이동한다.
이때, 양 비행기에서 다음으로 준비되는 부품의 시간이 동일하다면, 현재 트럭 위치의 부품을 먼저 싣는다.
만약, 현재 트럭이 있는 비행기가 모두 분해되었으면 반대쪽 비행기로 바로 이동해서 분해된 부품이 나올 때까지 대기한다.


    queue[flag][k] = ( 조립 완료 시간, 송장 번호 )
    각 부품 별 조립 완료 시간으로 Heap Q를 하고, 해당 부품의 배송 시작과 동시에 송장번호에 맞는 리스트의 0 번 자리에 시간 넣기
     -> 마찬가지로 배송 완료시, 송장번호에 맞는 리스트의 1번 자리에 시간 넣기.
    queue[flag] = [ (조립 완료 시간, 번호), (조립 완료 시간, 번호), ... ]

당신은 각 부품이 언제 출발했고, 언제 도착했는지에 대한 시간을 기록하고 싶다.
각 부품이 나오는 비행기의 번호와 부품의 무게, 운송이 준비되는 시간이 주어질 때, 각 부품이 출발하고 도착하는 시간을 순서대로 출력하자.
단, 부품이 분해된 경우 출발 시간은 분해된 부품이 최초로 출발한 시간, 도착시간은 분해된 부품들이 모두 반대편에 완전히 도착했을 때의 시간이다.




"""







import sys
import heapq
import math
input = sys.stdin.readline


N, M, T = map(int, input().split())
N, capacity, distance = int(N), int(M), int(T)
H_queue = [[], []]
ans_list = [[] for _ in range(N)]
for put_in in range(N):
    line = list(map(int, input().split()))
    if line[0] == 0:
        heapq.heappush(H_queue[0], (line[2], line[1], put_in))
    else:
        heapq.heappush(H_queue[1], (line[2], line[1], put_in))
    # H_queue에 빠른 순으로 (분해 시간, 용량, 번호) 튜플로 들어감
rotation = 0
time = 0
# 첫 시도는 따로 뺀다.
if


while H_queue != [[], []]:
    if time >= H_queue[rotation][0][0]:
        if H_queue[rotation][1] > capacity:
            H_queue[rotation][1] -= capacity
            time += distance
            rotation = (rotation+1)%2
        else:
            temp_capa = capacity - heapq.heappop(H_queue[rotation])[1]







for printing in range(N):
    print(*ans_list[printing])