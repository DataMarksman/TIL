# BOJ. 그냥 N M 시리즈 이거로 돌려막기 다했슴다
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline


def recur(X, idx):
    X = X[:]
    if len(X) == B:
        ans_list.append(X)
        return
    else:
        for pick in range(idx, A):
            recur(X + [num_list[pick]], pick)


A, B = map(int, input().split())
num_list = sorted(list(map(int, input().split())))
ans_list = []
recur([], 0)
ans_list.sort()
print(*ans_list[0])
for printing in range(1, len(ans_list)):
    if ans_list[printing] != ans_list[printing-1]:
        print(*ans_list[printing])