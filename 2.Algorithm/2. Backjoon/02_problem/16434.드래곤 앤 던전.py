# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N, ATK = map(int, input().split())
max_HP = 1
temp_HP = 1
for rooms in range(N):
    line = list(map(int, input().split()))
    if line[0] == 2:
        ATK += line[1]
        temp_HP = temp_HP + line[2] if max_HP - temp_HP >= line[2] else max_HP
    else:
        dealing = line[1] * (line[2]//ATK) if line[2]%ATK else line[1] * ((line[2]//ATK)-1)
        if temp_HP < dealing:
            max_HP += dealing - temp_HP + 1
            temp_HP = 1
        else:
            temp_HP -= dealing
print(max_HP)

"""
8 3
1 1 31
1 1 31
1 1 31
1 1 31
1 1 31
1 1 31
2 3 70
1 3 100

3 3
1 1 49
2 3 1
1 3 100
"""
