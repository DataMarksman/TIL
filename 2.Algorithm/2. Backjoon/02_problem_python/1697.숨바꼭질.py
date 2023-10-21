# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
start, goal = map(int, input().split())
goal_limit = goal * 2
bi_index = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024,
            2048, 4096, 8192, 16384, 32768, 65536, 131072]

if start == goal:
    print(0)
elif start >= goal:
    print(start - goal)
else:
    answer = 100001

    def find_diff(pre_idx, remain, steps):
        global answer
        if steps >= answer:
            return
        elif remain == 0:
            answer = min(steps, answer)
        elif pre_idx == 0:
            answer = min(steps + remain, answer)
        else:
            left_cnt = remain // bi_index[pre_idx]
            if remain % bi_index[pre_idx] == 0:
                if remain >= bi_index[pre_idx]:
                    answer = min(steps + left_cnt, answer)
                else:
                    find_diff(pre_idx - 1, remain - (left_cnt * bi_index[pre_idx]), steps + left_cnt)
                    find_diff(pre_idx - 1, ((left_cnt + 1) * bi_index[pre_idx]) - remain, steps + left_cnt)
            else:
                find_diff(pre_idx - 1, remain - (left_cnt * bi_index[pre_idx]), steps + left_cnt)
                find_diff(pre_idx - 1, ((left_cnt+1) * bi_index[pre_idx]) - remain, steps + left_cnt+1)
    start_flag = 0
    if start == 0:
        start = 1
        start_flag = 1
    left = int(start)
    right = int(start) * 2
    idx = 0
    while right <= goal:
        idx += 1
        left, right = right, right * 2
    left_remain = goal - left
    right_remain = right - goal
    find_diff(idx, left_remain, idx + start_flag)
    find_diff(idx+1, right_remain, idx + start_flag + 1)
    print(answer)

