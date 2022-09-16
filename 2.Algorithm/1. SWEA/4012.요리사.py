# SWEA.4012. 요리사
# 설계 목적: 역시 함수 하나로 끝장을 보고 싶은 재귀 성애자...
# 1. 먼저 N//2 의 길이를 가지는 부분 집합을 만들 때 까지는 계속 조합 만들기 재귀가 돌아갑니다.
# 2. 부분 집합. 즉 해당 조합의 길이가 N//2 에 도달하면, 해당 조합들에서 인자를 2개씩 꺼내서 맛의 합산을 구합니다.
# 3. 이렇게 구한 맛의 합과, 선택받지 못한 재료들에서 구한 맛의 합을 빼준 값을 ans 값과 비교하여 더 작으면 갱신합니다.
# 4. 끝

# 개선점:
# 1. 처음에 부분집합, 즉 조합을 만들 때,
#    for pick in range(N): 으로 진행하면 시간 초과 납니다.
#    for pick in range(K, N): 으로 해서 이전에 뽑은 거 다음부터 뽑게해서 중복 연산 안하도록 합시다.
# 2. 효율화 한답시고, 처음에 값 받을 때, 대각선 기준 좌 하단 값을 우상단에 합쳐서 받고, 재귀에서 한번에 불러왔는데...
#    -> 이거 시간 오히려 더 잡아먹습니다... 왜 인지 알려면 CS 공부가 필요할 듯 합니다.

def case_sort(K, pick_set):
    global ans
    pick_set = set(pick_set)
    if len(pick_set) == N // 2:
        A = list(pick_set)
        B = list(num_set-pick_set)
        sum_A = 0
        sum_B = 0
        for i in range((N//2)-1):
            for j in range(i+1, N//2):
                sum_A += board[A[i]][A[j]] + board[A[j]][A[i]]
                sum_B += board[B[i]][B[j]] + board[B[j]][B[i]]
        if abs(sum_A - sum_B) < ans:
            ans = abs(sum_A - sum_B)
    else:
        for pick in range(K+1, N):
            if pick not in pick_set:
                pick_set.add(pick)
                case_sort(pick, pick_set)
                pick_set.remove(pick)


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    num_set = set(list(i for i in range(N)))
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = 99999999999999
    case_sort(0, set())
    print(f'#{case_num} {ans}')