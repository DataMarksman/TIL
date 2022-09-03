# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
sys.setrecursionlimit(10**6)


def rooting(start, depth, arr):
    global max_ans
    if depth >= N:
        temp_idx = arr[0]
        temp_sum = 0
        temp_sum += num_list[0][arr[0]]
        for charging in range(1, depth):
            temp_sum += num_list[charging][arr[charging]] - num_list[charging][temp_idx]
            temp_idx = arr[charging]
        if temp_sum > max_ans:
            max_ans = temp_sum
    elif depth < N - 1:
        for picking in range(start, M):
            arr.append(picking)
            rooting(picking, depth+1, arr)
            arr.pop()
    elif depth == N - 1:
        arr.append(M-1)
        rooting(M-1, depth + 1, arr)


N, M = tuple(map(int, input().split()))
num_list = [[0]*M for _ in range(N)]
for put_in in range(N):
    lines = list(map(int, input().split()))
    for pile_up in range(1, M):
        lines[pile_up] = lines[pile_up-1]
    num_list += [lines]
max_ans = 0
rooting(0, 0, [])
print(max_ans)
