# 4408. 자기방으로 돌아가기

T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    hall = [0] * 401
    student_list = [list(map(int, input().split())) for _ in range(N)]
    for student in range(len(student_list)):
        for passing in range(student_list[student][0]+1, student_list[student][1]):
            hall[passing] += 1
    ans = max(hall)
    print(f'#{case_num} {ans}')
