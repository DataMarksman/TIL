
"""
input 예시
7 8  # Vertex = 7개, Edge = 8개인 그래프가 있을 때,
1 2  # 다음 8개의 줄에 연결 정보를 제공
1 3
2 4
2 5  # 2번과 5번이 양방향으로 연결되어 있음!
4 6
5 6
6 7
3 7
"""
V, E = map(int, input().split())

adj_matrix = [[0]*(V+1) for _ in range(V+1)]

# 바둑판 짜기~
for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

# adj_matrix print 결과

# [[0, 0, 0, 0, 0, 0, 0, 0],  => 0번 포도알은 존재하지 않음
#  [0, 0, 1, 1, 0, 0, 0, 0],  => 1번 포도알은 2, 3번으로 갈 수 있음
#  [0, 1, 0, 0, 1, 1, 0, 0],  => 2번 포도알은 1, 4, 5번 가능
#  [0, 1, 0, 0, 0, 0, 0, 1],  => 3번 포도알은 1, 7번 가능
#  [0, 0, 1, 0, 0, 0, 1, 0],  => 4번 포도알은 2, 6번 가능
#  [0, 0, 1, 0, 0, 0, 1, 0],  => 5번 포도알은 2, 6번 가능
#  [0, 0, 0, 0, 1, 1, 0, 1],  => 6번 포도알은 4, 5, 7번 가능
#  [0, 0, 0, 1, 0, 0, 1, 0]]  => 7번 포도알은 3, 6번 가능

Q = [1]
visited = []


# 스택이 빌 때 까지 돌아라~
while Q:
    current_idx = Q.pop(0)                            # Q 앞에서 하나 빼와서 지금 위치에 저장해줬!
    if current_idx not in visited:                    # 여기... 혹시 처음 오는 위치야?
        visited.append(current_idx)                   # 그럼~ visited 에 저장해야지~

        for destination in range(V+1):                # 여기에서 갈 수 있는 위치 (즉 값이 1인것)들을 뽑아볼까?
            if adj_matrix[current_idx][destination]\
                    and destination not in visited:   # 아, 물론 방문한적 없는 곳만
                Q.append(destination)                 # 그렇다면 -> Q에 저장!

