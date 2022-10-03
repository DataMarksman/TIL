# BOJ. 13414. 수강신청
# 설계 의도: 좀 더 빠르게!
# sys.stdin으로 받았더니 뒤에 \n 가 붙어나오죠? 프린트 할 때만 지워주면 됩니다. 끝.
# 개선점:
# 1. 더 빠르게 한 사람들은 대체 어떻게 한거지?
import sys
K, N = map(int, sys.stdin.readline().rstrip().split())
visited = set()
num_list = [sys.stdin.readline().rstrip() for _ in range(N)]
ans_list = []
for checking in range(N-1, -1, -1):
    if num_list[checking] in visited:
        continue
    else:
        visited.add(num_list[checking])
if len(ans_list) <= K:
    K = len(ans_list)
for printing in range(-1, -K - 1, -1):
    print(ans_list[printing])