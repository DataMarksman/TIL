# BOJ. 2116 주사위 쌓기
# 설계 의도: 길찾기와 동일.
# 1. 길 지나가면서, 내가 지나지 않은 길들 중 큰 값 같이 빼오기.
# 개선점: 리커전 한계치 올려줘야 한다.
# import sys
# sys.setrecursionlimit(10**6)
def dice_up(n, k, stock):                                         # 재귀용 함수
    global sum_list                                               # 바로 sum_list 에 넣어줍니다
    if n >= N:                                                    # 재귀 종료 조건을 주고
        sum_list += [sum(stock)]                                  # 지금 까지 쌓아둔 숫자의 합을 반환.

    elif n == 0:                                                  # 반약, 재귀 첫 시도라면,
        stock = []                                                # 쌓아두는 공간 초기화 시키고
        for idx in range(6):                                      # 첫 시작점 6개를 전부 고려한다.
            start = dice_list[n][idx % 3][idx % 2]                # 2차원 배열 전부 순회하는 idx 배치
            stock += [max(max(dice_list[n][(idx + 1) % 3]),
                          max(dice_list[n][(idx + 2) % 3]))]      # 가지 않은 길 두곳의 max 값 중 max 값 기입
            dice_up(n + 1, start, stock)                          # 깊이를 +1 하여 재귀
            stock = []                                            # 저장소 초기화

    else:
        for idx in range(6):                                      # 다음 주사위의 6개의 눈 중에서
            if dice_list[n][idx % 3][idx % 2] == k:               # 이전 재귀에서 뽑아온 [시작 지점]과 일치
                start = dice_list[n][idx % 3][(idx + 1) % 2]      # 다음 [시작 지점]은 이전 [시작 지점] 반대편
                stock += [max(max(dice_list[n][(idx + 1) % 3]),
                              max(dice_list[n][(idx + 2) % 3]))]  # 가지 않은 길 두곳의 max 값 중 max 값 기입
                return dice_up(n + 1, start, stock)


N = int(input())                                                  #
dice_list = [[] for _ in range(N)]                                #
sum_list = []                                                     #
# sum_list = [28, 27, 27, 25, 28, 25]
for put_in in range(N):                                           #
    num_list = list(map(int, input().split()))                    #
    dice_list[put_in] += [[num_list[0], num_list[5]]]             # 1번째 양면 리스트로 입력
    dice_list[put_in] += [[num_list[1], num_list[3]]]             # 2번째 양면 리스트로 입력
    dice_list[put_in] += [[num_list[2], num_list[4]]]             # 3번째 양면 리스트로 입력
    # dice_list = [[[2, 4], [3, 6], [1, 5]], [[3, 5], [1, 4]...
dice_up(0, 0, [])                                                 # 재귀 ( 0의 깊이, 시작 숫자 0, 빈공간 )
print(max(sum_list))                                              #
