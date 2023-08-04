# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
original = sys.stdin.readline().rstrip()
text = sys.stdin.readline().rstrip()
N = len(original)
length = len(text)
ans = 0
top = 0
check_set = set(list(original))
for get_check in range(2, N+1):
    for get_word in range(0, N-get_check+1):
        check_set.add(original[get_word:get_word+get_check])

while top < length:
    for greedy in range(N, 0, -1):
        if text[top:top + greedy] in check_set:
            ans += 1
            top += greedy
            if length - top < N:
                N = int(length - top)
            break
print(ans)