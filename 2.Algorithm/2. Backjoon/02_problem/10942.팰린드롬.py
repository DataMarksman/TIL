# BOJ. 10942. 펠린드롬
# 설계 의도:
# 이게 DP? 잘 모르겠네요
# 개선점:
# 좀 더 빠르게 못하나?
import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
check_list = [[0]*(N-i) for i in range(N)]

# S 즉, 스타트 지점은 0 ~ N-1 입니다.
for S in range(N):

    # 각 스타트 지점에서 펠린드롬을 찾기 위해 갈 수 있는 최대 거리를 구합니다.
    limit = min(S+1, N-S)
    # 해당 시작 지점을 중심으로 홀수 자리수의 팰린드롬을 구합니다.
    # 각 거리에 맞춰, 해당 거리에 있는 값들이 같으면, 계속 팰린드롬임을 입력해줍니다.
    for adding in range(1, limit):
        if num_list[S-adding] == num_list[S+adding]:
            check_list[S-adding][adding*2] = 1
        # 한번이라도 아니면, 다음도 아니므로 Break 걸어줍니다.
        else:
            break

    # 해당 시작 지점을 중심으로 짝수 자리수의 팰린드롬을 구합니다.
    # 각 거리에 맞춰, 해당 거리에 있는 값들이 같으면, 계속 팰린드롬임을 입력해줍니다.

    if S < N-1:
        # 우선, 현재 내 위치와 다음 위치가 같은지 확인해줍니다.
        if num_list[S] == num_list[S+1]:
            # 맞으면 짝수 팰린을 진행합니다.
            check_list[S][1] = 1
            for adding_2 in range(1, limit):
                if S + adding_2 < N-1:
                    if num_list[S - adding_2] == num_list[S + adding_2 + 1]:
                        check_list[S - adding_2][(adding_2 * 2) + 1] = 1
                    else:
                        break
# print(check_list)
# 값을 입력 받고 바로 출력해줍니다.
T = int(input())
for tc in range(T):
    S, E = map(int, input().split())
    print(check_list[S-1][E - S])


