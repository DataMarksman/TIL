# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T+1):
    N, M = map(int, input().split())
    N = int(N)
    M = int(M)
    box_list = []
    for _ in range(N):
        box_list.append(int(input()))
    sec = 0
    done_count = 0
    while done_count < M:
        sec += 1
        print(f'여기! {sec}초 경과시')
        done_count = 0
        for boxes in box_list:
            done_count += (sec//boxes)
            print(f'{boxes}짜리 박스에서 {sec//boxes}명 해결')
    print(f'#{case_num} {sec}')
