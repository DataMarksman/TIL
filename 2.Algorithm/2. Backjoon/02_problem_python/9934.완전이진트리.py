# BOJ. 9934. 완전 이진트리
# 설계 의도: 조건에 맞는 실행
# 0. 탐색할 장소의 조건인 Max(거점 번호) 값인 N을 구한다.
# 1. 먼저 중위 탐색을 위한 재귀함수를 작성한다.
# 1.1. 이 재귀함수의 depth는 층수를 의미한다.
# 2. 먼저 밟을 때마다 value 리스트에서 앞의 값을 빼서 현재 위치에 저장해준다.
# 3. 이렇게 트리를 작성하면, 층별로 출력해준다.


def rooting(point, depth):                     # 중위 탐색 구현용 재귀 함수
    global tree_list
    if point <= N:
        rooting(point*2, depth + 1)            # 다음 왼쪽

        pick = value_list.pop(0)               # 밟을 때마다 value 리스트의 앞의 값을 빼오면 된다.
        tree_list[depth].append(pick)

        rooting((point*2)+1, depth + 1)        # 다음 오른쪽


K = int(input())
value_list = list(map(int, input().split()))
N = max(value_list)
tree_list = [[] for _ in range(K)]
rooting(1, 0)
for printing in range(K):
    print(*tree_list[printing])