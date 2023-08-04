# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = sys.stdin.readline

T = int(input())
for case_num in range(T):
    A, B = map(int, input().split())
    target = B - A
    ans = 0
    while True:
        if target >= (ans+1)*2:
            target -= (ans+1)*2
            ans += 1
        elif target > ans+1:
            ans = (ans+1)*2
            break
        elif target == 0:
            ans *= 2
            break
        else:
            ans = ans*2 + 1
            break
    print(ans)

"""
24
1 5
45 50
0 2147483647
3 2000000000
20 23
0 2147483647
1 2147483647
2 2147483647
41706 2147483647
41707 2147483647
2147483643 2147483647
2147483644 2147483647
2147483645 2147483647
2147483646 2147483647
0 1
0 2
0 3
0 4
0 6
0 7
0 9
0 12
0 14
0 15
"""