# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
length = int(sys.stdin.readline().rstrip())
gun_range, power = map(int, sys.stdin.readline().rstrip().split())
bomb_count = int(sys.stdin.readline().rstrip())
miss_count = set()
survive_flag = True
for shooting in range(1, length + 1):
    zombie = int(sys.stdin.readline().rstrip())
    if survive_flag:
        if miss_count:
            miss_sum = 0
            temp_miss_count = set()
            while miss_count:
                miss_shot = miss_count.pop()
                if miss_shot > 0:
                    miss_sum += power
                    temp_miss_count.add(miss_shot-1)
            if temp_miss_count:
                miss_count = set(temp_miss_count)
            zombie += miss_sum

        if shooting < gun_range:
            if shooting * power < zombie:
                if bomb_count > 0:
                    bomb_count -= 1
                    miss_count.add(gun_range-1)
                else:
                    survive_flag = False
        else:
            if gun_range * power < zombie:
                if bomb_count > 0:
                    bomb_count -= 1
                    miss_count.add(gun_range-1)
                else:
                    survive_flag = False
if survive_flag:
    print("YES")
else:
    print("NO")


