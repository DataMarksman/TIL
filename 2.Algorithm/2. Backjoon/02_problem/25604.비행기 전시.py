# BOJ. 25604. 비행기 전시
# 설계 의도: 그냥 빡 구현
# 개선점:
# 1. 우왕 1등이당
# 2. 각 Queue 들이 살아있는지 수시로 확인해야 인덱스 에러 안납니당 주의

import sys
import heapq
input = sys.stdin.readline


N, M, T = map(int, input().split())
N, capacity, delay = int(N), int(M), int(T)
H_queue = [[], []]
ans_list = [[] for _ in range(N)]
for put_in in range(N):

    # H_queue[배당 전시관]에 빠른 순으로 (분해 시간, 번호, 용량) 튜플로 들어감
    line = list(map(int, input().split()))
    if line[0] == 0:
        heapq.heappush(H_queue[0], [line[2], put_in, line[1]])
    else:
        heapq.heappush(H_queue[1], [line[2], put_in, line[1]])

position = 0
now = 0
while H_queue[0] != [] or H_queue[1] != []:

    # 루틴 들어가면서 리셋할 것들: 트럭 용량
    volume = int(capacity)

    # 0. 이 쪽 대기열 남은거 있음? 확인하고 들어가기
    if H_queue[position]:
        # 1. 시간 확인. 현 위치의 다음 타겟 시간이 현재 시간보다 작다면 GO, 아니라면 if문 진입
        if H_queue[position][0][0] > now:
            # 1.1 저쪽 라인 살아있니?
            if H_queue[(position+1) % 2]:
                # 1.1.1 저쪽 대기열도 now 보다 길게 남아있으면 둘 중 차이 적은 쪽 만큼 더해주기 다음 루틴 진입
                if H_queue[(position+1) % 2][0][0] > now:
                    now += min(H_queue[position][0][0] - now, H_queue[(position + 1) % 2][0][0] - now)
                # 1.1.2 저쪽 대기열은 바로 가능하면 그쪽으로 그냥 이동.
                else:
                    now += delay
                    position = (position + 1) % 2
            # 1.2 저쪽 라인 죽었으면 뭐... 여기서 기다려야지.
            else:
                now = H_queue[position][0][0]

        # 2. 시간 문제 넘어가면, 물건 올리기 루트 진입
        else:
            # 2.0 한계치 까지 물건을 쌓아 올려봅시다.
            while volume > 0 and H_queue[position]:
                no_idx = H_queue[position][0][1]
                time_check = H_queue[position][0][0]
                if time_check > now:
                    break
                if not ans_list[no_idx]:
                    ans_list[no_idx] += [now]
                if volume >= H_queue[position][0][2]:
                    volume -= H_queue[position][0][2]
                    ans_list[no_idx] += [now + delay]
                    if H_queue[position]:
                        heapq.heappop(H_queue[position])
                    else:
                        break
                else:
                    H_queue[position][0][2] -= volume
                    volume = 0
            now += delay
            position = (position + 1) % 2

    # 0. 이쪽 대기열 비어있으면 바로 다른 쪽으로 이동하기
    else:
        now += delay
        position = (position + 1) % 2

# 송장번호 순서대로 인쇄하기.
for printing in range(N):
    print(*ans_list[printing])