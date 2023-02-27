# 임시 저장용 String Answer
answer_string = "9" * 100
answer_length = 100
memo_root = []


def solution(edges, target):
    global answer_string
    global answer_length
    # 길이 값
    length = len(target)

    # 목표 값
    target_sum = sum(target)



    # 각 노드에 연결된 자식 노드들의 리스트
    child_node_list = [[] for i in range(length+1)]

    # 각 노드에 연결된 자식 노드들의 개수
    child_count = [0]*(length+1)

    # 각 노드를 순회하면서 밟을 친구들 idx
    child_idx_list = [0]*(length+1)

    # 각 리프 노드를 밟는 순서를 기입

    for node_union in edges:
        father = node_union[0]
        child = node_union[1]
        child_node_list[father].append(child)
        child_count[father] += 1

    for rearrange in range(1, length+1):
        child_node_list[rearrange].sort()

    # 루트 노드부터 시작해서 내려오는 방향 탐색용
    def find_root_way(t):
        # 만약 메모이즘 된 depth가 있다면 그것을 반환합니다.
        if t < len(memo_root):
            return memo_root[t]
        else:
            while t >= len(memo_root):
                top = 1
                while True:
                    if not child_count[top]:
                        memo_root.append(top)
                        break
                    else:
                        top, child_idx_list[top] = child_node_list[top][child_idx_list[top]], (child_count[top]+1)%child_count[top]]
            return memo_root[t]

    def find_leaf_root(pre_pick, temp_answer, t, k):
        global answer_string
        global answer_length
        if t > answer_length:
            return

        elif k == target_sum:
            if int(answer_string) > int(temp_answer):
                answer_string = temp_answer
                answer_length = t

        else:
            find_root_way(t)
            for pick_number in [3, 2, 1]:
                if pick_number != pre_pick and target[t] >= pick_number:
                    target[t] -= pick_number
                    find_leaf_root(pick_number, temp_answer + str(pick_number), t + 1, k + pick_number)
                    target[t] += pick_number
            else:
                return

    find_leaf_root(0, '', 0, 0)

    answer = []

    if answer_string == "9"*100:
        answer.append(-1)
    else:
        for answering in range(answer_length):
            answer.append(int(answer_string[answering]))
    return answer

print(solution([[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]], [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]))