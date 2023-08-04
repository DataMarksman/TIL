# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
count_list = [0]*(max(num_list)+1)
for numbers in range(N):
    count_list[num_list[numbers]] += 1
compare_list = []
ans_list = []
for searching in range(N-1, -1, -1):
    for checking in range(len(compare_list)):
        if count_list[compare_list[checking]] > count_list[num_list[searching]]:
            ans_list.insert(0, compare_list[checking])
            break
    else:
        ans_list.insert(0, -1)
    compare_list.insert(0, num_list[searching])
print(*ans_list)
