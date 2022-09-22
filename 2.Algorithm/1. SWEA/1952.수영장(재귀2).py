# SWEA. 1952 수영장
# 설계 목적: 재귀 함수
# 1. 처음에 1~12월의 값을 받고 각 달의 값 * 일일 이용권 가격과 월간 이용권 가격을 비교.
# 2. 더 싼곳으로 리스트를 채워놓은 다음 본격적으로 재귀에 들어간다.
# 3. 우선 1~12월을 돌면서 연속한 3개월의 수치의 합이 TM 미만인 곳을 셋으로 빼고
# 4. 이렇게 추려낸 셋을 리스트에 넣어서 재귀로 조합을 만든다.
# 5. 만들어진 조합에서 가장 작은 값과 연간 이용권 가격을 비교한 다음 더 작은 것을 답으로 출력

# 재귀의 가능성은 무한하다는 것을 보여주기 위한 퍼포먼스였고,
# DP로도 풀겠습니다.

# 재귀.. 이거 퇴마가 필요하다.
def tm_judge(visited, start, count):
    global ans
    visited = set(visited)                  # 갱신용 ans의 global 선언. 및 set id 초기화
    for picking in range(start, len(TM_list)):
        if not TM_list[picking] & visited:  # 조합 만들기
            tm_judge(visited | TM_list[picking], picking + 1, count + 1) # 셋 연산자 사용
    my_ans = sum(month_list) + (count * TM)
    while visited:
        pick = visited.pop()
        my_ans -= month_list[pick]
    if my_ans < ans:                         # 조합으로 만든 값이 더 작으면 ans 갱신
        ans = my_ans


T = int(input())
for case_num in range(1, T + 1):
    D, M, TM, Y = map(int, input().split())
    month_list = list(map(int, input().split()))
    for m_check in range(12):                # 받은 month_list의 각 값을
        if month_list[m_check]*D > M:        # 일간 이용권 x 날짜 와 월간 이용권 중
            month_list[m_check] = M          # 더 저렴한 쪽으로 바꿔줌
        else:
            month_list[m_check] *= D
    TM_list = []                             # idx 기반으로 조합을 만들기에 리스트로 제작
    ans = sum(month_list)                    # 갱신용 변수, 초기값은 현재의 총합
    for TM_check in range(10):
        if sum(month_list[TM_check:TM_check+3]) > TM:
            TM_list.append({TM_check, TM_check+1, TM_check+2})
    if sum(month_list[10:12]) > TM:
        TM_list.append({10, 11})
    if month_list[11] > TM:
        TM_list.append({11, })
    tm_judge(set(), 0, 0)
    if ans > Y:                              # 3개월 이용권 적용 최저값과 연간 이용권 비교
        ans = Y
    print(f'#{case_num} {ans}')