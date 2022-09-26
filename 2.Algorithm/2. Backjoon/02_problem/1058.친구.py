# BOJ. 1058 친구
# 설계 의도: 배수 그래프 열화버전의 열화버전
# 1. 현재 행idx에서 갈 수 있는 or 친구인. == 'Y' 열idx를 set에 담고
# 2. 해당 set의 인자들을 하나씩 빼고 해당 인자들을 행idx로 하는 행을 순회하면서 == 'Y'을 찾기
# 3. 이것들을 모아놓은 set의 길이가 2- 친구의 명수, 단 이때 처음에 제시된 본인은 걸러야함.
# 개선점:
# 백트 걸면 더 빨라질 것 같긴 한데, 이미 충분한게 아닐까 싶습니다.
# python3 기준 88ms

N = int(input())
friend_list = [list(input()) for _ in range(N)]
max_friend = 0
for checking in range(N):
    friend_set = set()
    count_set = set()
    for first_F in range(N):
        if friend_list[checking][first_F] == 'Y':
            friend_set.add(first_F)
    else:
        while friend_set:
            pick = friend_set.pop()
            count_set.add(pick)
            for second_F in range(N):
                if friend_list[pick][second_F] == 'Y' and second_F != checking:
                    count_set.add(second_F)
    if len(count_set) > max_friend:
        max_friend = int(len(count_set))
print(max_friend)

