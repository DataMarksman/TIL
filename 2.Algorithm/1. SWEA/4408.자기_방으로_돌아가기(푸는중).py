# 4408. 자기방으로 돌아가기

def rooting(list_st, count):
    if len(list_st) == 0:
        return print(f'#{case_num} {count}')
    count += 1
    hall = [0]*400
    remain_list = []
    for student in range(len(list_st)):

        for passing in range(list_st[student][0], list_st[student][1]+1):
            if hall[passing] == 1:
                remain_list += [list_st[student]]
                break
        else:
            for passing in range(list_st[student][0], list_st[student][1]+1):
                hall[passing] = 1
    return rooting(remain_list, count)


T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    student_list = [list(map(int, input().split())) for _ in range(N)]
    rooting(student_list, 0)