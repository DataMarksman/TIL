# SWEA.
# 설계 목적: 연산 최적화
# 1. set을 두개 만든다. 하나는 A set, 두번째는 B set
# 2. 각 세트를 순회하면서 하나 빼보고 -1 -1 혹은 -1 +1 혹은 +1 +1 있으면 그거 통과. 없으면 len(set)>2 일때까지 뽑기
# 3. 자, 처음 순회가 실패하겠죠? 그러면 이제 시작입니다.
# 개선점:
# 1.

# import sys
# sys.stdin = open("sample_input.txt", "r")

from itertools import combinations, combinations_with_replacement


def check_ans(input_set, discard_set):
    if ans < 0:
        discard_set = set(discard_set)
        input_set = set(input_set)
        flag = True
        for rows in range(height):
            if flag:
                flag = False
                compare_set = set(check_set[rows])
                compare_set |= input_set
                compare_set -= discard_set
                for numbering in range(wide-K+1):
                    P = {p for p in range(numbering, numbering+K)}
                    if P & compare_set == P or P & compare_set == set():
                        flag = True
                        break
            else:
                break
        if flag:
            return True
        else:
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
            if ans < 0:
                pick_set = set(combinations(pick_list, incur))
                while pick_set and ans < 0:
                    pick = set(pick_set.pop())
                    for recur in range(len(pick)):
                        if ans < 0:
                            part_set = set(combinations_with_replacement(list(pick), incur))
                            while part_set:
                                part1 = set(part_set.pop())
                                part2 = pick - part1
                                if check_ans(part1, part2):
                                    ans = incur
                                    break
                            if check_ans(set(), pick):
                                ans = incur
                        else:
                            break
            else:
                break
    print(f'#{case_num} {ans}')


