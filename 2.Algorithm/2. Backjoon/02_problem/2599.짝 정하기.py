# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
# import sys
# sys.setrecursionlimit(10**6)

N = int(input())
AM, AW = map(int, input().split())     # AM 은 BW와 CW로 분배 된다! 즉 AM = BW + CW
BM, BW = map(int, input().split())     # 이하 동일한데, 범위도 줄 수 있다. AM <= BW, AM <= CW
CM, CW = map(int, input().split())     # 그러면 이제, AM을 AM = A + (AM - A) 로 표현해보자.
if AM <= BW + CW and BM <= AW + CW and CM <= AW + BW and (AM + BM + CM) == (AW + BW + CW):
    for checking in range(max(1, AM-BW), min(AM, CW)+1):
        A = checking                   # A가 올 수 있는 가장 좁은 범위 내에서의 A 순회다!
        B = CW - A                     # A가 정해지면 B, C도 정해진다!
        C = BW - (AM - A)
        # if AW == (BM - B) + (CM - C):  # 그런 즉, 확실하게 정해지는 B, C 말고, 이걸 통해 T/F 여부 확인 가능한 식을 대입하면 끝
        print(f'1 \n{AM - A} {A}\n{BM - B} {B}\n{CM - C} {C}')
        break
    else:
        print(0)
else:
    print(0)