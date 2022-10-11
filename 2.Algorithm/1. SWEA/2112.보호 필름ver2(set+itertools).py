# SWEA.
# 설계 목적: SET 연산 비교
# 1. 요컨데 0이 연속 K개 있거나 1이 연속 K개 있으면 된다?
# 2. 바로 옆으로 뒤집어 줍니다. 어짜피 연속성이 중요한 것.
# 3. [커트] 바로 확인해서 정답이면 0, K == 1 이면 0 출력.
# 4. 이후 1 부터 wide(원본값 = 높이)만큼 하나씩 늘려가면서 조합으로 적용

# < 확인용 함수 로직 >
# i) 각 층 (옆으로 돌렸으니 원래는 column) 을 순회하면서, 연속된 숫자가 3개 있는지 체크하기
# ii) 중간에 하나라도 없으면 False 반환.
# iii) 끝까지 다 돌면 True 반환

# 중간에 확인용 함수에서 True 반환되면 바로 종료.

# 개선점:
# 1. 호올리 ㅋㅋㅋㅋㅋㅋㅋ 속도 4자리수 실화인가...
from itertools import combinations


def check_ans(input_set, discard_set):
    input_set = set(input_set)
    discard_set = set(discard_set)
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
            return False
    if flag:
        return True


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
    elif K == 1:
        ans = 0
    else:
        pick_list = [i for i in range(wide)]
        for incur in range(1, wide):
            pick_set = set(combinations(pick_list, incur))
            while pick_set and ans < 0:
                pick = set(pick_set.pop())
                if check_ans(set(), pick) or check_ans(pick, set()):
                    ans = incur
                    break
                else:
                    for picking in range(1, len(pick)):
                        part_set = set(combinations(list(pick), picking))
                        while part_set:
                            part1 = set(part_set.pop())
                            part2 = pick - part1
                            if check_ans(part1, part2):
                                ans = incur
                                break
            if ans >= 0:
                break
    if ans == -1:
        ans = wide
    print(f'#{case_num} {ans}')


