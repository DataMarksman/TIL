# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:

N = int(input())
AM, AW = map(int, input().split())
BM, BW = map(int, input().split())
CM, CW = map(int, input().split())
if AM <= BW + CW and BM <= AW + CW and CM <= AW + BW and AM + BM + CM == AW + BW + CW:
    print(f'1 \n{BW} {AM - BW}\n{BM - CW + AM - BW} {CW - AM + BW}\n{CM} {0}')
else:
    print(0)