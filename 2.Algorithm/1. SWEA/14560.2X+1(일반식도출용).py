# import sys
# sys.stdin = open("sample_input.txt", "r")
"""
num_list = list(map(int, input().split()))
A_N = num_list[0]
A_P = num_list[1]
A_C = num_list[2]

B_N = num_list[3]
B_C = num_list[4]
"""

# 제조기 만들기:
# x, y 두가지로 구성된 리스트.
# 이것을 0,1로 바꿔서 순열로 구성한다. 단, 0의 개수와 1의 개수는 동일하다.
# 즉, 2*n개의 요소를 가진다. depth 가 1 커질 수록 길이는 2씩 증가.

def finding(n):
    global ans_list
    flag = True
    while flag:
        count_xy = [n, n]
        for pick in range(2):
            count_xy[pick] -= 1






    if (B_C-A_C)/A_P == 7:
        return ans_list
    else:
        finding(n+1)

A_N = 1
A_P = 1
A_C = 0

B_N = 1
B_C = 0
print(f'A: {A_N}N + {A_P}P + {A_C}, B: {B_N}N + {B_C}')

ans_list = []

while True:
    key = input()
    if key == 'x':
        A_C += 1
        B_N *= 2
        B_C *= 2
    elif key == 'y':
        A_N *= 2
        A_P *= 2
        A_C *= 2
        B_C += 1
    elif key == 'n':
        break
    else:
        continue
    print(f'A: {A_N}N + {A_P}P + {A_C}, B: {B_N}N + {B_C} -> P = {(B_C-A_C)/A_P if A_N == B_N else None}')






"""
T = int(input())
for case_num in range(1, T+1):
    A, B = tuple(map(int, input().split()))
    ans = str('')
    while A // B != 2:
        if A == B:
            break
        elif A > B and A // B > 2:
            A = A+1
            B = B*2
            ans += 'X'
        elif A > B and A // B == 1:
            A = A*2
            B = B+1
            ans += 'Y'
        elif A < B:
            A = A * 2
            B = B + 1
            ans += 'Y'
    T = A % B
    ans += 'YX'*T
    ans += 'X'
    print(f'#{case_num} {ans}')
"""

