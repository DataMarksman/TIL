# SWEA.
# 설계 목적:
# 1.
# 개선점:
# 1. 코드 잘못 짬.
# 2. 문제 이해 잘못 함.
# 3. 실전이었으면 이거 1시간 통으로 날린거다.
# 4. 확실하게 조건 전부 정리하고 어떻게 구현할지 고민한 다음에 코드 짜야 손실이 없다.


def shuffle(n):
    global deck_1
    global deck_2
    for cards in range(n):
        deck_1[point-n], deck_2[n] = deck_2[n], deck_1[point-n]

def compare(k):
    k += 1
    count_forward = [0]*N
    count_backward = [0]*N
    for cards in range(point):
        if deck_1[(point-1)-cards] == compare_deck_1[(point-1)-cards]:
            count_forward[cards] = 1
        elif deck_1[(point-1)-cards] == compare_deck_2[cards]:
            count_backward[(N-1)-cards] = 1

        if deck_2[cards] == compare_deck_2[cards]:
            count_forward[(point-1) + cards] = 1
        elif deck_2[cards] == compare_deck_1[(point-1) - cards]:
            count_backward[(point-1) - cards] = 1
    print(count_forward)
    print(count_backward)
    if sum(count_forward) >= sum(count_backward):
        return count_forward
    else:
        return count_backward

T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    card_list = list(map(int, input().split()))
    point = N // 2
    deck_1 = card_list[:point]
    deck_2 = card_list[point:]
    print(card_list)
    print(deck_1)
    print(deck_2)
    count = 0
    compare_deck_1 = [i for i in range(1, point+1)]
    compare_deck_2 = [j for j in range(point+1, (2*point)+1)]

    print(compare(0))


    """
    if count <= 5:
        ans_list = deck_1 + deck_2
    if ans_list == compare_deck_1 + compare_deck_2 or ans_list == compare_deck_2[::-1] + compare_deck_1[::-1]:
        print(f'#{case_num} {count}')
    else:
        print(f'#{case_num} {-1}')
    """