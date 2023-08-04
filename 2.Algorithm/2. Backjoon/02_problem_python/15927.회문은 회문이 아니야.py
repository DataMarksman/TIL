# BOJ. 15927. 회문은 회문이 아니야.
# 설계 의도: 뒤집어 보고 확인하기. 이게.. 골드?
# 개선점:
import sys
input = sys.stdin.readline
ans = -1
word = input().rstrip()
length = len(word)
if len(set(list(word))) == 1:
    print(-1)
else:
    while length > 0:
        if word == word[::-1]:
            length -= 1
            word = word[:length]
        else:
            ans = len(word)
            break
    print(ans)