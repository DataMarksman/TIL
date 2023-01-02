# SWEA.
# 설계 목적: 연산 최적화
# 1. set을 두개 만든다. 하나는 A set, 두번째는 B set
# 2. 각 세트를 순회하면서 하나 빼보고 -1 -1 혹은 -1 +1 혹은 +1 +1 있으면 그거 통과. 없으면 len(set)>2 일때까지 뽑기
# 3. 자, 처음 순회가 실패하겠죠? 그러면 이제 시작입니다.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")


T = int(input())
for case_num in range(1, T + 1):
    wide, height, K = map(int, input().split())
    lines = [list(map(int, input().split())) for _ in range(wide)]
    board = list(map(list, zip(*lines)))
    check_set = [set(), set()]
    ans = 0
    flag = True
    while True:

        for rows in range(height):
            if flag:
                flag = False
                for columns in range(wide-2):
                    if board[rows][columns] == board[rows][columns+1] == board[rows][columns+2]:
                        flag = True
                        break
            else:
                break
        else:
            break
        if

    print(f'#{case_num} {ans}')