# BOJ.
# 설계 의도: 조건에 맞는 실행
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
check_set = [[{0,2,3,4,5,6,7,8,9,}, {0,2,3,5,6,7,8,9,}, {0,1,2,3,4,5,6,7,8,9,}],
             [{0,4,5,6,8,9,}, set(), {0,1,2,3,4,7,8,9,}],
             [{0,2,3,4,5,6,8,9,}, {2,3,4,5,6,8,9,}, {0,1,2,3,4,5,6,7,8,9,}],
             [{0,2,6,8,}, set(), {0,1,3,4,5,6,7,8,9,}],
             [{0,2,3,5,6,8,9,}, {0,2,3,5,6,8,9,}, {0,1,2,3,4,5,6,7,8,9,}]]


num_list = [1,2,3,4,5,6,7,8,9,0]
N = int(input())
my_number = [set(num_list) for j in range(N)]
board = [[] for _ in range(N)]
for put_in in range(5):
    line = list(input())
    for checking in range(N):
        for window in range(3):
            if my_number[checking]:
                if line[(checking*4) + window] == '#':
                    my_number[checking] &= check_set[put_in][window]
            else:
                break
count = 1
for first_check in range(N):
    if not my_number[first_check]:
        ans = -1
        break
    else:
        count *= len(my_number[first_check])
else:
    ans = 0
    for summing in range(N):
        multiple = count / len(my_number[summing])
        while my_number[summing]:
            pick = my_number[summing].pop()
            ans += pick*(10**((N-1)-summing))*multiple
    ans /= count
print(ans)

