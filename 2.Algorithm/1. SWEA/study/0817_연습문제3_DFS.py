V, E = map(int, input().split())
adj_matrix = [[0]*(V+1) for _ in range(V+1)]
idx_list = list(map(int, input().split()))
for i in range(E):
    adj_matrix[idx_list[2*i]][idx_list[(2*i)+1]] = 1
    adj_matrix[idx_list[(2*i)+1]][idx_list[2*i]] = 1
stack = [1]
visited = []
while stack:
    current_idx = stack.pop()                        # 스택에서 꽁무니 하나 빼와서 지금 위치에 저장해줬!
    if current_idx not in visited:                   # 여기... 혹시 처음 오는 위치야?
        visited.append(current_idx)                  # 그럼~ visited 에 저장해야지~
        for destination in range(V+1):               # 여기에서 갈 수 있는 위치 (즉 값이 1인것)들을 뽑아볼까?
            if adj_matrix[current_idx][destination]\
                    and destination not in visited:  # 아, 물론 방문한적 없는 곳만
                stack.append(destination)            # 그렇다면 -> 스택에 저장!
print(visited)

