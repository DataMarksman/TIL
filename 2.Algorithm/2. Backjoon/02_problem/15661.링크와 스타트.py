# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

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


N = int(input())
num_set = set(list(i for i in range(N)))
board = [list(map(int, input().split())) for _ in range(N)]
ans = 99999999999999
case_sort(0, set())
print(ans)