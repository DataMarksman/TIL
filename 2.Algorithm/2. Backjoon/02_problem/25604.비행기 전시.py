# BOJ.
# 설계 의도:
# [파기] [0]*(math.ceil(10000/T)) 로 만들어서 최적화 하자 -> 중간에라도 운송 가능하면 해야함. 파기.
# [파기]
# 1. 단, 부품이 분해된 경우 출발 시간은 분해된 부품이 최초로 출발한 시간, 도착시간은 분해된 부품들이 모두 반대편에 완전히 도착했을 때의 시간이다.
# 개선점:
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