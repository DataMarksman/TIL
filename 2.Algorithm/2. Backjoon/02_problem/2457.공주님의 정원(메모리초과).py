# BOJ.
# 설계 의도: 조건에 맞는 실행
# 각 월별 날짜 리스트 만들고 해당 월만큼 슬라이싱하면, 이전 달의 일수만큼 커버 가능.
# 이러면 1차원 리스트로 계산 가능해지는 이점이 있다.
# 1. 본격적인 풀이는 set()을 기반으로 한다.
# 2. 각각의 범위들을 구해줬으면, 해당 범위 안에 속하는 숫자들을 set으로 만들어준다.
# 3. 순열을 통해 각각의 set을 합집합 했을 때, 가장 적은 수로 범위 내의 모든 숫자를 다 가지는 조합을 찾는다.
# 4. 백트래킹은 이미 나온 숫자보다 커지면 커팅하는 식으로 준다.
# 5. 배트래킹 2는 이 리스트들을 저장할때, 그 길이가 긴 것들부터 내림차순으로 정리하는 것으로 한다.
# 개선점:
import itertools
import sys
sys.setrecursionlimit(10**6)


def flowering(arr):
    flag = False
    while arr:
        A = arr.pop()
        check_set = set()
        for flowers in A:
            check_set |= flower_list[flowers]
        if len(check_set) >= 274:
            flag = True
            arr = []
            break
    if flag:
        return True


# 결국 275일동안 피어있으면 되는건데...
month_count = [31,28,31,30,31,30,31,31,30,31,30,31]
flower_list = [[] for _ in range(367)]
N = int(input())
for case_num in range(1, N+1):
    line = list(map(int, input().split()))
    A = sum(month_count[:line[0]-1]) + line[1]
    B = sum(month_count[:line[2]-1]) + line[3]
    if A > 334:
        continue
    if B < 59:
        continue
    if A <= 59:
        A = 60
    if B >= 336:
        B = 335
    flower_list.append(set(int(_) for _ in range(A, B)))

ans = 0
num_list = [k for k in range(len(flower_list))]
for checking in range(1, len(flower_list)+1):
    check_list = list(itertools.combinations(num_list, checking))
    if flowering(check_list):
        ans = checking
print(ans//2)

