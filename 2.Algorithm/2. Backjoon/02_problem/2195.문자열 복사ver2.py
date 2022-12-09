# BOJ. 2195. 문자열 복사
# 설계 의도: 앞에서부터 가장 긴거 빼나아가기
# 개선점:
# 1. 처음에는 나올 수 있는 경우의 수를 Set으로 빼서 넣었는데, 사실 string 이라 그럴 필요가 없었다.
# 2. 이 방법론보다 빠른 방법론이 분명 존재할 것....
import sys
original = sys.stdin.readline().rstrip()
text = sys.stdin.readline().rstrip()
N = len(original)
ans = 0

# 제시된 글을 앞에서부터, 찾고자 하는 단어와 매칭 되는 가장 킨 부분을 제거해나아간다.
while text:
    for greedy in range(N, 0, -1):
        if text[:greedy] in original:
            ans += 1
            text = text[greedy:]

            # 제시된 글의 남은 부분이 찾고자 하는 단어보다 작으면 검색 범위를 좁혀준다.
            if len(text) < N:
                N = len(text)
            break
print(ans)