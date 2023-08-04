# BOJ. 1654. 랜선자르기
# 설계 의도: 이분 탐색...
# 개선점:
# 많이 느리다. 더 빠르게 하고 싶다.
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


# 특정 값으로 각 선들을 잘랐을 때, 몇개가 나오는지 뽑아내는 함수
def find_ans(x):
    temp_ans = 0
    for check in range(N):
        temp_ans += num_list[check]//x
        # 백트래킹입니다. 중간에 이미 Goal보다 커지면 거기서 탐색 종료합니다.
        if temp_ans >= Goal:
            return True
    else:
        return False


N, Goal = map(int, input().split())
# 백트를 위해 내림차순 정렬
num_list = sorted([int(input()) for _ in range(N)], reverse=True)

# 시작은 1로 시작. 어짜피 최소 1로 나눠야 할테니.
left = 1
# 내림차순 정렬한 것의 첫번째 값이므로, 0 도출
right = num_list[0]

# 커팅 되나?
if right == 1:
    print(1)
else:
    # 이분 탐색 진행
    mid = (left+right)//2

    # 이건, Goal 개를 만들수 있는 가장 큰 수를 구하는 것이므로
    # left가 끝에 걸치게 하고 right로 좌로 넘어가면 된다.
    while left <= right:
        mid = (left+right)//2
        if find_ans(mid):
            left = int(mid) + 1
        else:
            right = int(mid) - 1
    print(right)
