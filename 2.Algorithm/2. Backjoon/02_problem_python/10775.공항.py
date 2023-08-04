# BOJ. 10775. 공항
# 설계 의도: 한번 갔던 곳은 워프 시켜버리자~
# 1. 예시를 들어보자. N 번 포트까지 착륙 시킬 수 있으면 N번 포트부터 내려오면서 채워야 한다.
# 2. 그러나 4번 포트짜리 2, 3번 포트 짜리 2이 들어온 다음에 1번 포트 하나가 들어오면 어떻게 4번 포트에서 넘쳤는지 알 수 있나?
# 3. 이러한 관점에서, 이미 사용한 포트를 한번에 알 수 있으려면 jump 리스트로 0 아래로 내려가는 경우를 구해야한다.
# 개선점:
# 느리다? union 같은거 안쓰고 최대한 main 내에서 한 것 같은데...
import sys
input = sys.stdin.readline


def dump():
    return int(input())


Gate = int(input())
Plane = int(input())
jump = [i for i in range(Gate+1)]
ans = 0
for rending in range(Plane):
    get_gate = int(input())

    # 처음 뽑는 거니? 그러면 그냥 뽑아
    if jump[get_gate] == get_gate:
        change = get_gate

    # 이미 와봤던 곳이야? 그러면 워프 돌려
    else:
        change = jump[get_gate]
        while jump[change] != change:
            change = jump[change]

    # 워프 된 곳에서 하나 뺀 곳으로 다음 워프 좌표 지정
    jump[get_gate] = change - 1

    # 워프 된 지점은 이미 사용했으니 -1 해주자구.
    jump[change] = change - 1

    # 바닥까지 싹싹 긁었으면 멈추고 나머지는 dumping 하자.
    if jump[0] == -1:
        for dumping in range(Plane - rending - 1):
            dump()
        break
    else:
        ans += 1
print(ans)