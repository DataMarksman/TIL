# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')


def depth_finding(k):
    top = int(k)
    depth_cnt = 0
    while top != 1:
        depth_cnt += 1
        top = parents_list[top]
    return depth_cnt


N = int(input())
parents_list = [0]*(N+1)
leaf_nodes_set = set(i for i in range(1, N+1))
layer_set = [{1}, set()]
layer_top = 0
for i in range(N-1):
    U, V = map(int, input().split())
    leaf_nodes_set.discard(U)
    parents_list[V] = U
    if U in layer_set[layer_top]:
        layer_set[layer_top+1].add(V)
    else:
        layer_top += 1
        layer_set.append({V})
if len(layer_set[1]) == 1:
    leaf_nodes_set.add('1')

start_node = 0
start_depth = int(layer_top)
cnt_sum = 0
pick_flag = True
aim_parents_set = set()
# print("leaf_set: ", leaf_nodes_set)
while start_depth >= 1:
    # print("layer_depth : ", start_depth)
    # print("layer_set : ", layer_set[start_depth])
    # print("pick_flag : ", pick_flag)
    if pick_flag:
        cnt_sum += len(layer_set[start_depth] - leaf_nodes_set)
        tmp_parents_nodes_set = set(layer_set[start_depth] & leaf_nodes_set)
        while tmp_parents_nodes_set:
            aim_parents_set.add(parents_list[tmp_parents_nodes_set.pop()])

        pick_flag = False
        # print("aim_set: ", aim_parents_set)
    else:
        cnt_sum += len(aim_parents_set)
        aim_parents_set = set()
        pick_flag = True
    start_depth -= 1
    # print("present_cnt!!!!!!: ", cnt_sum)
    # print("==============================")

print(cnt_sum)


# while leaf_nodes_set:
#     pick = leaf_nodes_set.pop()
#     colored_nodes.add(parents_list[pick])
#     depth = depth_finding(pick)
#     if depth > start_depth:
#         start_depth = depth
#         start_node = pick


""""
5
1 5
2 5
3 5
4 5

"""