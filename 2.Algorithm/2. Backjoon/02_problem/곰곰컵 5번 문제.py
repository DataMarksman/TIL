# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
N = int(sys.stdin.readline().strip())
ans = 0
Plague_Flag = False
Dancing_people = set()
for case in range(N):
    Get_dance = set(sys.stdin.readline().strip().split(' '))
    if Plague_Flag and Dancing_people & Get_dance:
        Dancing_people |= Get_dance
    else:
        if "ChongChong" in Get_dance:
            Plague_Flag = True
            Dancing_people |= Get_dance
print(len(Dancing_people))
