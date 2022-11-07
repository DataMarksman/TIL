# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline
N, ATK = map(int, input().split())
ATK = int(ATK)
max_HP = 1
temp_HP = 1
temp_heal = 0
for rooms in range(N):
    line = list(map(int, input().split()))
    if line[0] == 2:
        ATK += line[1]
        if temp_HP < max_HP:
            if max_HP - temp_HP >= line[2]:
                temp_HP += line[2]
            else:
                temp_heal += line[2] - (max_HP - temp_HP)
                temp_HP = int(max_HP)
        else:
            temp_heal += line[2]
    else:
        enemy_ATK = line[1]
        enemy_HP = line[2]
        while True:
            enemy_HP -= ATK
            if enemy_HP <= 0:
                break
            else:
                if enemy_ATK >= temp_HP + temp_heal:
                    max_HP += abs(enemy_ATK - (temp_HP + temp_heal))+1
                    temp_heal = 0
                elif enemy_ATK >= temp_HP:
                    max_HP += abs(enemy_ATK - temp_HP)+1
                else:
                    temp_HP -= enemy_ATK
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
