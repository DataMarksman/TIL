# 2477. 참외밭
# 설계 의도:
# 1. 이 문제는 반시계 방향으로 돌면서 순서대로 길이를 제시한다.
#   즉, 같은 방향 패턴이 두번 나오면 그것이 안쪽으로 들어갔다 나온 패턴이다.
#   현재로서 세련된 방법을 모르겠으니, 그냥 두번 입력하고 한번 분량만큼 탐색하자.
# 개선점: 범위를 벗어나 반복되는 패턴을 한방에 캐치할 수 없을까?

K = int(input())
len_list = [list(map(int, input().split())) for _ in range(6)]
check_len = len_list[:]*2
small_area = 0
large_area = 0
# len_list = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]
# check_len = [[4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100],
#               [4, 50], [2, 160], [3, 30], [1, 60], [3, 20], [1, 100]]

# 2배 길이의 체크용 리스트에서 한번 분량만 돌리면 반복 패턴 캐치 가능.
# 반복문: 이번 패턴이 이 다음 패턴과 일치하고, 그 다음 패턴과는 불일치하는 시작점 탐색
for checking in range(6):
    if check_len[checking][0] == check_len[checking+2][0] and\
            check_len[checking+1][0] == check_len[checking + 3][0] and\
            check_len[checking][0] != check_len[checking+4][0] and\
            check_len[checking+1][0] != check_len[checking+5][0]:
        small_area = check_len[checking+1][1]*check_len[checking+2][1]
        large_area = check_len[checking+4][1]*check_len[checking+5][1]
# large_area = 8000
# small_area = 1200
ans = (large_area-small_area)*K
print(ans)