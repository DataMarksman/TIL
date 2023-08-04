# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().split()))
mid = num_list.index(max(num_list))
ans = 0
list_1 = num_list[:mid][::-1]
list_2 = num_list[mid+1:]
while list_1:
    target = max(list_1)
    idx = list_1.index(target)
    for summing in range(idx):
        ans += target - list_1[summing]
    list_1 = list_1[idx+1:]
while list_2:
    target = max(list_2)
    idx = list_2.index(target)
    for summing in range(idx):
        ans += target - list_2[summing]
    list_2 = list_2[idx+1:]
print(ans)
