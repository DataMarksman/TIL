# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1. 각 범위를 쪼개면서 내려가자.
# 2. 범위 길이 N이 짝수면 반으로 갈라서 좌, 우의 리턴 값을 함수에서 비교
# 3. 범위 길이가 홀수면 가장 오른쪽 것과 그것을 제외한 나머지 길이의 값을 함수에서 비교
# 4. 가장 작은 단위는 길이 2짜리로 본다. 첫 값
def game(s, e):
    if (e - s) == 2:
        a = member_queue[s]
        b = member_queue[s+1]
        if a[0] == b[0]:
            return a if a[1] < b[1] else b
        elif (a[0] + b[0]) % 2 == 0:
            return a if a[0] < b[0] else b
        elif (a[0] + b[0]) % 2 == 1:
            return a if a[0] > b[0] else b
    elif (e-s)%2 == 1:
        ans = game(game(s, e-1)

    ans = game(s, e//2)
    return ans





T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    member_queue = []
    for members in range(1, N+1):
        P = num_list.pop(0)
        member_queue.append((P, members))

    print(f'#{case_num} {member_queue[0][1]}')
