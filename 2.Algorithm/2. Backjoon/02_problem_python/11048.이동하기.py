# BOJ. 11048 이동하기.
# 설계 의도: DP! 길찾기 문제의 전형적인 예시
# 1. 만약, 완전탐색으로 모든 경로를 다 검색해서 구하려고 하면 시간초과 납니다. 해봄.
# 2. 각각 루트에서의 최선의 선택을 찾아 나아가는 방식을 채용합니다.
# 3. <루틴> 자신의 왼쪽 혹은 위쪽의 값 중 큰 값을 자신이 있는 위치의 값과 더해서 자신의 위치에 저장합니다.
# 4. 이러한 루틴을 반복하면 마지막에는 최선의 이동 경로에서 구해진 최대 값이 도출됩니다.
#    최저값도 같은 방식으로 구할 수 있습니다.
# 개선점:
# 1. 모든 문제가 완전탐색은 아닙니다. 효율화에 조금 더 신경 써봅시다.

# 위? 혹은 왼쪽.
dx = [-1, 0]
dy = [0, -1]

N, M = tuple(map(int, input().split()))
num_list = [list(map(int, input().split())) for _ in range(N)]
ans_list = [[0]*M for _ in range(N)]
for x in range(N):
    for y in range(M):
        tmp_sum = 0
        if 0 <= x-1:
            if ans_list[x-1][y] > tmp_sum:
                tmp_sum = ans_list[x-1][y]
        if 0 <= y-1:
            if ans_list[x][y-1] > tmp_sum:
                tmp_sum = ans_list[x][y-1]
        ans_list[x][y] = num_list[x][y] + tmp_sum
print(ans_list[N-1][M-1])
