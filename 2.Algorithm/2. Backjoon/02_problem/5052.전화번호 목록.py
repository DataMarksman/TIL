# BOJ. 5052 전화번호 목록
# 설계 의도: 확인용 set과 뽑기용 sorted된 리스트 만들어서 뽑으면서 확인하기
# 개선점: 느리네요... ㅠ ㅠ
import sys
T = int(sys.stdin.readline().rstrip())
for tc in range(1, T+1):
    N = int(sys.stdin.readline().rstrip())
    numbers = set()
    ans_flag = True
    for get_numb in range(N):
        number = sys.stdin.readline().rstrip()
        numbers.add(number)

    check_list = sorted(numbers)
    while check_list and ans_flag:
        pick = check_list.pop()
        numbers.discard(pick)
        for check in range(1, len(pick)+1):
            if pick[:check] in numbers:
                ans_flag = False
                break
    if ans_flag:
        print('YES')
    else:
        print('NO')