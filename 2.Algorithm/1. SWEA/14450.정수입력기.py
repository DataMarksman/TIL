# SWEA. 14450. 정수 입력기
# 설계 목적: 이거 자리수 문제 아님?
# 1. 일단 스트링으로 받아서 좌(A) 우(B) 값의 길이를 산출합니당.
# 2. 길이 차이 별로 구해야하는 방법이 달라지므로, 분기합니다.
# 개선점:
# 1. 오 1등~
T = int(input())
for case_num in range(1, T + 1):

    # 길이 빼줄거니까 input 으로 받습니다.
    A, B, N = input().split()

    # ans 는 스트링으로 만들어주고, 답을 쌓아올려줍니다
    ans = ''
    num_list = list(input().split())

    # 각각 최소값의 길이와 최대값을 길이을 빼주고 다시 전부 int로 바꿔줍니당
    dif_A = len(A)
    dif_B = len(B)
    A = int(A)
    B = int(B)
    N = int(N)

    # 숫자를 하나씩 살펴봅니다
    for checking in range(N):

        # 숫자의 길이와 정수 형태의 값을 빼줍니다.
        length = len(num_list[checking])
        number = int(num_list[checking])

        # 그냥 쌩 값이 B보다 크면 당연히 아웃이죠?
        if number > B:
            ans += 'X'

        # 최소, 최대값의 길이가 같을 경우에는 각각의 값들을 비교값과 같은 길이로 만들어주고, 비교합니다.
        # 어짜피 모든 수가 올 수 있기 때문에, 비교 대상이 되는 최대, 최소값의 아래자리 수들은 상관 없슴당.
        elif dif_A == dif_B:
            if (A // 10 ** (dif_A - length)) <= number <= B // (10 ** (dif_B - length)):
                ans += 'O'
            else:
                ans += 'X'

        # 차이가 1인 경우에는 A와 같은 길이로 가서 A보다 크거나 혹은 B와 같은 길이로 가서 B보다 작은지 보면 됩니다.
        # 둘 중 하나만 맞아도 통과입니다.
        elif dif_B - dif_A == 1:
            if (A // 10 ** (dif_A - length if dif_A - length > 0 else 0)) <= number \
                    or number <= B // (10 ** (dif_B - length)):
                ans += 'O'
            else:
                ans += 'X'

        # 그 외의 경우에는 길이 차이가 2 이상인 경우이므로, 쉽게 말해서 본래의 B보다 작으면 다 됩니당.
        else:
            if number <= B:
                ans += 'O'
            else:
                ans += 'X'
    print(f'#{case_num} {ans}')


"""

10
310 341 6
2 3 31 39 33 333
1 9 6
1 2 3 10 20 30
123 456 5
5 40 777 456 3
999 1001 3
98 102 1000
9500 18872 12
4 10 15 60 90 98 188 2000 6000 18872 20000 19000
440 520 15
1 2 3 4 5 6 7 8 9 10 30 40 47 54 150
990000000 1900000000 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
35 267 3
40 27 247
1 199999 3
2 3 4
97 1230 4
96 10 11 12

#1 XOOXOO
#2 OOOXXX
#3 XOXOO
#4 XXO
#5 XOOXXOOXXOXX
#6 XXXOOXXXXXXXOXX
#7 OXXXXXXXOOOOOOOOOOOX
#8 OXO
#9 OOO
#10 OOOO
"""