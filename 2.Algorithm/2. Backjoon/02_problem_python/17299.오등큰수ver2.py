# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
count_list = [0]*1000001
for numbers in range(N):
    count_list[num_list[numbers]] += 1
ans_list = []
compare_list = []
for searching in range(N-1, -1, -1):
    for checking in range(len(compare_list)-1, -1, -1):
        if count_list[compare_list[checking]] > count_list[num_list[searching]]:
            ans_list += [compare_list[checking]]
            compare_list = compare_list[:checking+1] + [num_list[searching]]
            break
    else:
        compare_list = [num_list[searching]]
        ans_list += [-1]
print(*ans_list[::-1])
