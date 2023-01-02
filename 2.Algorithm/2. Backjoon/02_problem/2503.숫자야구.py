# 강환석
# 이건 그냥 대입하는게 빠릅니다. 숫자가 더 커지면 모를까...
# 설계 의도: 하나씩 맞춰보기
# 1. 먼저 갓 itertools로 가능한 모든 경우의 수를 빼줍니다.
# 2. 그걸 test 함수에 넣고, 각 조건들이 맞는지 체크해나갑니다.
# 3. 중간에 하나라도 틀리면 0반환, 끝까지 다 돌면 1 반환
# 4. 이렇게 나온 값의 합계를 출력
import sys
import itertools


def test(check_list):
    for checking in range(N):
        count_strike = 0
        for hit in range(3):
            if check_list[hit] == number_list[checking][hit]:
                count_strike += 1
        if count_strike == strike_list[checking]:
            count_ball = len(set(check_list) & set(number_list[checking])) - count_strike
            if count_ball == ball_list[checking]:
                pass
            else:
                return 0
        else:
            return 0
    else:
        return 1


N = int(sys.stdin.readline())
ans = 0
number_list = []
strike_list = []
ball_list = []
for put_in in range(N):
    A, B, C = sys.stdin.readline().split()
    number_list += [[int(A[0]), int(A[1]), int(A[2])]]
    strike_list += [int(B)]
    ball_list += [int(C)]
base_set = set(itertools.permutations([i for i in range(1, 10)], 3))
while base_set:
    ans += test(base_set.pop())
print(ans)