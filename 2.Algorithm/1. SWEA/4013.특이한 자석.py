# SWEA. 4013.특이한 자석
# 설계 목적:
# 1. 그냥 돌려요. 재귀에 넣어줄 것: 현재 기어 번호, 도는 방향, 왼쪽or오른쪽
# 2. 첫 재귀는 LR에다가 좌우 다 넣어주고, 다음부터는 방향성 주고 돌리면 됩니다.
# 3. 처음에 옆의 기어들이 같이 돌아가는지 여부 확인하고 한번에 돌리는거라
#     -> 먼저 확인 쫙 해주고 돌리는 절차 들어갑니다~
# 개선점:
# 1.문제는 쉬웠는데 재귀 함수에서 k+1 을 안써줘서 계속 디버깅.
def spinning(k, direction, LR):
    global gear_list

    if k + 1 < 4 and 'R' in LR:
        if gear_list[k][2] != gear_list[k+1][6]:
            spinning(k+1, direction * (-1), "R")
    if k - 1 >= 0 and 'L' in LR:
        if gear_list[k][6] != gear_list[k-1][2]:
            spinning(k-1, direction * (-1), "L")

    if direction > 0:
        gear_list[k] = [gear_list[k][7]] + gear_list[k][:7]
    elif direction < 0:
        gear_list[k] = gear_list[k][1:] + [gear_list[k][0]]


T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    gear_list = [list(map(int, input().split())) for _ in range(4)]
    for spin_trial in range(N):
        A, B = map(int, input().split())
        spinning(A-1, B, "LR")
    ans = 0
    for checking in range(4):
        if gear_list[checking][0] == 1:
            ans += 2**checking
    print(f'#{case_num} {ans}')

"""
1
2
0 0 1 0 0 1 0 0
1 0 0 1 1 1 0 1
0 0 1 0 1 1 0 0
0 0 1 0 1 1 0 1
1 1
3 -1

1
2
1 0 0 1 0 0 0 0
0 1 1 1 1 1 1 1
0 1 0 1 0 0 1 0
0 1 0 0 1 1 0 1
3 1
1 1

"""