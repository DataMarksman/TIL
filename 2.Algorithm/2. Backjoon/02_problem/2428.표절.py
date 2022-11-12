# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort(reverse=True)
count = 0

for i in range(len(num_list) - 1):
    if num_list[i] * 0.9 <= num_list[-1]:
        count += len(num_list) - 1 - i
        continue

    start = i + 1
    end = len(num_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if num_list[mid] >= num_list[i] * 0.9:
            start = mid + 1
        else:
            end = mid - 1
    count += end - i
print(count)