# SWEA.
# 설계 목적: 연산 최적화
# 1. set을 두개 만든다. 하나는 A set, 두번째는 B set
# 2. 각 세트를 순회하면서 하나 빼보고 -1 -1 혹은 -1 +1 혹은 +1 +1 있으면 그거 통과. 없으면 len(set)>2 일때까지 뽑기
# 3. 자, 처음 순회가 실패하겠죠? 그러면 이제 시작입니다.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")

from itertools import combinations


def check_ans(discard_set, input_set):
    if ans < 0:
        discard_set = set(discard_set)
        input_set = set(input_set)
        flag = True
        for rows in range(height):
            if flag:
                flag = False
                compare_set = set(check_set[rows])
                compare_set -= discard_set
                compare_set |= input_set
                for numbering in range(wide-2):
                    if {numbering, numbering+1, numbering+2} & compare_set == {numbering, numbering+1, numbering+2} or\
                            {numbering, numbering+1, numbering+2} & compare_set == set():
                        flag = True
                        break
            else:
                break
        else:
            if flag:
                return True
            else:
                return False
        return False
    else:
        return False


T = int(input())
for case_num in range(1, T + 1):
    wide, height, K = map(int, input().split())
    check_set = [set() for _ in range(height)]
    for number in range(wide):
        line = list(map(int, input().split()))
        for story in range(height):
            if line[story]:
                check_set[story].add(number)
    ans = -1
    if check_ans(set(), set()):
        ans = 0
    else:
        pick_list = [i for i in range(wide)]
        for incur in range(1, wide):
            pick_set = set(combinations(pick_list, incur))
            while pick_set:
                pick = list(pick_set.pop())
                for recur in range(len(pick)):
                    

    print(f'#{case_num} {ans}')


