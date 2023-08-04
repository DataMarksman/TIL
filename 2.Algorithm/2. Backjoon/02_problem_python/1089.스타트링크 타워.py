# BOJ. 1089. 스타트 링크 타워
# 설계 의도: 각 위치에 # 이 들어가는 번호의 셋을 구성해서 교집합으로 지워나가기
# 개선점:

"""

###...#.###.###.#.#.###.###.###.###.###
#.#...#...#...#.#.#.#...#.....#.#.#.#.#
#.#...#.###.###.###.###.###...#.###.###
#.#...#.#.....#...#...#.#.#...#.#.#...#
###...#.###.###...#.###.###...#.###.###

"""

import sys
input = sys.stdin.readline

# 각 위치 좌표별 해당하는 비교용 셋을 만듭니다.
check_set = [[{0,2,3,4,5,6,7,8,9,}, {0,2,3,5,6,7,8,9,}, {0,1,2,3,4,5,6,7,8,9,}],
             [{0,4,5,6,8,9,}, set(), {0,1,2,3,4,7,8,9,}],
             [{0,2,3,4,5,6,8,9,}, {2,3,4,5,6,8,9,}, {0,1,2,3,4,5,6,7,8,9,}],
             [{0,2,6,8,}, set(), {0,1,3,4,5,6,7,8,9,}],
             [{0,2,3,5,6,8,9,}, {0,2,3,5,6,8,9,}, {0,1,2,3,4,5,6,7,8,9,}]]


# 처음에 들고갈 기본 셋 입니다. 여기에서 각 위치 좌표의 셋과 비교해가면서 값을 쳐냅니다.
num_list = [1,2,3,4,5,6,7,8,9,0]
N = int(input())
my_number = [set(num_list) for j in range(N)]
board = [[] for _ in range(N)]

# 5줄을 3칸씩 비교하는 것이므로, range(5) 입니당
for put_in in range(5):
    line = list(input())
    for checking in range(N):
        for window in range(3):
            if my_number[checking]:
                if line[(checking*4) + window] == '#':                # 해당 위치에 # 이 있으면
                    my_number[checking] &= check_set[put_in][window]  # 위치 좌표의 셋과 교집합
            else:
                break
count = 1                          # 곱연산으로 구해줄 것이므로, 1을 기본값으로 합니다.
for first_check in range(N):
    if not my_number[first_check]:
        ans = -1                   # 한칸이라도 만들 수 있는 숫자가 없는 칸이 있으면 -1을 출력해줍니다.
        break
    else:
        count *= len(my_number[first_check])  # 전체 케이스의 수를 곱연산으로 구합니다
else:                              # 가/불가 체크가 끝났으면 합연산에 들어갑니다
    ans = 0                        # 합연산의 기본값이므로 0으로 시작합니다.
    for summing in range(N):
        multiple = count / len(my_number[summing])    # 이 위치에서 나오는 수가 등장 가능한 횟수입니다.
        while my_number[summing]:
            pick = my_number[summing].pop()
            ans += pick*(10**((N-1)-summing))*multiple   # 가능한 값 * 10**N과 그 수가 나올수 있는 케이스를 곱해줍니당
    ans /= count
print(ans)   # 답 출력

