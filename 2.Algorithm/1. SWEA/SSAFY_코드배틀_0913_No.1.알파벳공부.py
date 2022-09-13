# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1. 코드 잘못 짬.
# 2. 문제 이해 잘못 함.
# 3. 실전이었으면 이거 1시간 통으로 날린거다.
# 4. 확실하게 조건 전부 정리하고 어떻게 구현할지 고민한 다음에 코드 짜야 손실이 없다.

T = int(input())
for tc in range(1, T+1):
    count = 0
    alpha = input()
    for checking in range(len(alpha)):
        if ord(alpha[checking])-97 == checking:
            count += 1
        else:
            break
    print(f'#{tc} {count}')




