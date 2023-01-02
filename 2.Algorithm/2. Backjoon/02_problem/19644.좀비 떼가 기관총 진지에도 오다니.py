# BOJ. 19644. 좀비 떼가 기관총 진지에도 오다니
# 설계 의도: 연산 효율화 기반 N번 연산으로 끝내기
# 1. 중요한 것은 Bomb을 사용했을때의 효율화다.
#   - range만큼 딜이 감소하므로 set에 사라지는 좌표를 넣어놓으면 1번의 연산으로 계산이 가능해진다.
# 2. bomb 다 떨어진 상태에서 딜 부족이면 그냥 넘기는게 이득.

# 개선점: 뭔가 다른 방법론으로 하면 더 빠를 것 같은데 모르겠다.
# def miis(): return map(int,input().split())
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

def ii():
    return int(input())


length = int(input())
gun_range, power = map(int, sys.stdin.readline().split())
bomb_count = int(sys.stdin.readline())
miss_count = set()
survive_flag = True
stop_count = length + 1
for shooting in range(1, length + 1):
    if not survive_flag:
        stop_count = shooting
        break
    else:
        zombie = int(sys.stdin.readline())
        miss_count.discard(shooting)
        if shooting < gun_range:
            if (shooting - len(miss_count)) * power < zombie:
                bomb_count -= 1
                miss_count.add(shooting + gun_range)
                if bomb_count < 0:
                    survive_flag = False
        else:
            if (gun_range - len(miss_count)) * power < zombie:
                bomb_count -= 1
                miss_count.add(shooting + gun_range)
                if bomb_count < 0:
                    survive_flag = False
for dumping in range(stop_count, length + 1):
    ii()


if survive_flag:
    print("YES")
else:
    print("NO")


