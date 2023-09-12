# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')
chip_cnt = [0]*10
chip_idx = {"B": 0,
            "R": 1,
            "O": 2,
            "N": 3,
            "Z": 4,
            "E": 5,
            "S": 6,
            "I": 7,
            "L": 8,
            "V": 9
            }
N = int(input())
chips = input()
for check in chips:
    if check in chip_idx.keys():
        chip_cnt[chip_idx[check]] += 1
chip_cnt[1] //= 2
chip_cnt[5] //= 2
print(min(chip_cnt))

