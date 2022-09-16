# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1. 아니, board는 101로 만들어놓고 탐색 range(100)으로 해놓은거 실화냐

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = 10
for case_num in range(1, T + 1):
    N, start = tuple(map(int, input().split()))
    board = [[0]*101 for _ in range(101)]
    input_list = list(map(int, input().split()))
    for put_in in range(N//2):
        board[input_list[put_in*2]][input_list[put_in*2 + 1]] = 1
    ans = 0
    visited = set()
    visited.add(start)
    call_queue = set()
    call_queue.add(start)
    while call_queue:
        ans = max(call_queue)
        size = len(call_queue)
        new_queue = set()
        for checking in range(size):
            caller = call_queue.pop()
            for calling in range(101):
                if board[caller][calling] == 1 and calling not in visited:
                    new_queue.add(calling)
                    visited.add(calling)
        call_queue = set(new_queue)
    print(f'#{case_num} {ans}')
