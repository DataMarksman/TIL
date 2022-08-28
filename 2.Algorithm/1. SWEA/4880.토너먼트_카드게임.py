# SWEA. 4880.토너먼트 카드게임
# 설계 목적:
# 1. 각 범위를 쪼개면서 내려가자.
# 2. 범위 길이 N이 짝수면 반으로 갈라서 좌, 우의 리턴 값을 함수에서 비교
# 3. 범위 길이가 홀수면 가장 오른쪽 것과 그것을 제외한 나머지 길이의 값을 함수에서 비교
# 4. 가장 작은 단위는 길이 2짜리로 본다.

# 개선점:
# 1. 요소가 하나짜리인 리스트도 만들어질 수 있는데, 리스트는 기본적으로 마지막에 , 을 넣어줘야 한다.
#       이거 빼먹으면 iterable한 리스트가 아니라 int로 반환된다... 요 주의
# 2. [중요] 문제의 조건을 그대로 구현할 생각을 해야한다.
#       len(arr)//2가 아니라, (첫 숫자 + 끝 숫자)//2 이다.
#       효율화? 이런건 우선사항이 아니다. 확실하게 문제에서 요구하는 사항을 구현하는 것이 먼저다.
def game(arr):
    if arr:
        alpha = len(arr)
        if alpha == 1:
            return [arr[0], ]
        elif alpha == 2:
            A = arr[0]
            B = arr[1]
            if num_list[A] == num_list[B]:
                return [A, ] if A < B else [B, ]
            elif (num_list[A] + num_list[B]) % 2 == 0:
                return [A, ] if num_list[A] < num_list[B] else [B, ]
            elif (num_list[A] + num_list[B]) % 2 == 1:
                return [A, ] if num_list[A] > num_list[B] else [B, ]
        else:
            return game(game(arr[:(1+alpha)//2]) + game(arr[(1+alpha)//2:]))


T = int(input())
for case_num in range(1, T+1):
    N = int(input())
    num_list = [0] + list(map(int, input().split()))
    students_list = [i for i in range(1, N+1)]
    answer = game(students_list)
    print(f'#{case_num}', *answer)