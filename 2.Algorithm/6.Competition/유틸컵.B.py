# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
target_Y, target_M, target_D = map(int, input().split("-"))
N = int(input())
answer = 0
for tc in range(N):
    Y, M, D = map(int, input().split("-"))
    if Y > target_Y:
        answer += 1
    elif Y < target_Y:
        continue
    else:
        if M > target_M:
            answer += 1
        elif M < target_M:
            continue
        else:
            if D >= target_D:
                answer += 1
print(answer)
