# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")
dx = [-0.5, 0, 0.5, 0]
dy = [0, 0.5, 0, -0.5]


T = int(input())
for case_num in range(1, T + 1):
    N, M, K = map(int, input().split())
    wide = N
    time = 2*M
    ans = 0
    board = [[0]*wide for _ in range(wide)]
    bug_list = []
    for put_in in range(K):
        A, B, C, D = map(int, input().split())
        if D == 1:
            New_D = 0
        elif D == 2:
            New_D = 2
        elif D == 3:
            New_D = 3
        else:
            New_D = 1
        bug_list += [[C, [A, B], New_D]]
    time_pass = 0
    bug_list.sort(reverse=True)
    print(bug_list)
    while time_pass < time:
        new_bug_list = []
        for bugs in range(len(bug_list)):
            bug_list[bugs][1][0] += dx[bug_list[bugs][2]]
            bug_list[bugs][1][1] += dy[bug_list[bugs][2]]
            if bug_list[bugs][1][0] == 0 or bug_list[bugs][1][0] == (wide-1) or\
                    bug_list[bugs][1][1] == 0 or bug_list[bugs][1][1] == (wide-1):
                bug_list[bugs][0] //= 2
                bug_list[bugs][2] = (bug_list[bugs][2]+2) % 4
            else:
                for checking in range(bugs):
                    if bug_list[bugs][1] == bug_list[checking][1] and bug_list[bugs][0] < bug_list[checking][0]:
                        bug_list[checking][0] += bug_list[bugs][0]
                        bug_list[bugs][0] = 0
                        break
        for killing in range(len(bug_list)):
            if bug_list[killing][0] != 0:
                new_bug_list.append(bug_list[killing])
        new_bug_list.sort(reverse=True)
        time_pass += 1
        print(time_pass, new_bug_list)

    for summing in range(len(bug_list)):
        ans += bug_list[summing][0]
    print(f'#{case_num} {ans}')

"""
1
7 2 9   
1 1 7 1 
2 1 7 1
5 1 5 4
3 2 8 4 
4 3 14 1
3 4 3 3 
1 5 8 2 
3 5 100 1
5 5 1 1
"""