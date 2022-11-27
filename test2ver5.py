# 문제 설계: 이거 완전 게리멘더링인데...
# 문제는 내가 게리멘더링을 못풀었음.
import itertools
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def rootchecking(idx, visited):
    visited = set(visited)
    checked_set = {idx, }
    Queue = {idx, }
    while Queue:
        start_idx = Queue.pop()
        for checking in range(N):
            if board[start_idx][checking] == 1 and checking not in visited and checking not in checked_set:
                Queue.add(checking)
                checked_set.add(checking)
    if set(checked_set | visited) == set(check_set):
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    aim_ans = 0
    ans = 99999999999

    check_set = set(i for i in range(N))
    board = [list(map(int, input().split())) for _ in range(N)]
    popularity = list(map(int, input().split()))
    bounty = sum(popularity)
    numset = set()
    combi_list = [i for i in range(N)]
    for making in range(1, ((N+1)//2)+1):
        numset |= set(itertools.combinations(combi_list, making))

    while numset:
        pick = set(numset.pop())
        subpick = set(pick)
        start = set(check_set - pick).pop()
        if rootchecking(start, pick) and rootchecking(subpick.pop(),set(check_set - pick)):
            temp_value = 0
            while pick:
                numbs = pick.pop()
                temp_value += popularity[numbs]
            if abs(bounty - (temp_value)*2) < ans:
                ans = abs(bounty - (temp_value)*2)
    print(f"#{tc} {ans}")


"""
10
4
0 0 1 0
0 0 1 0
1 1 0 1
0 0 1 0
6 7 4 8
5
0 1 0 1 0
1 0 1 1 1
0 1 0 0 0
1 1 0 0 1
0 1 0 1 0
10 10 3 10 7
6
0 1 0 0 0 1
1 0 0 1 1 1
0 0 0 1 0 0
0 1 1 0 0 0
0 1 0 0 0 0
1 1 0 0 0 0
13 18 8 5 18 5
6
0 1 1 1 1 0
1 0 0 0 1 0
1 0 0 0 1 0
1 0 0 0 0 1
1 1 1 0 0 1
0 0 0 1 1 0
17 11 7 15 4 11
7
0 1 0 0 0 0 1
1 0 0 0 0 1 1
0 0 0 0 0 1 1
0 0 0 0 1 0 0
0 0 0 1 0 1 1
0 1 1 0 1 0 0
1 1 1 0 1 0 0
15 18 14 9 7 7 12
7
0 1 0 1 0 1 0
1 0 0 1 0 0 0
0 0 0 0 0 1 0
1 1 0 0 1 0 0
0 0 0 1 0 1 1
1 0 1 0 1 0 0
0 0 0 0 1 0 0
20 20 3 12 6 16 13
7
0 1 0 0 1 0 0
1 0 0 0 1 1 1
0 0 0 1 0 1 0
0 0 1 0 1 0 0
1 1 0 1 0 0 0
0 1 1 0 0 0 0
0 1 0 0 0 0 0
9 16 16 12 19 18 4
7
0 0 0 0 1 1 0
0 0 0 0 0 1 1
0 0 0 1 0 1 1
0 0 1 0 1 1 0
1 0 0 1 0 0 1
1 1 1 1 0 0 0
0 1 1 0 1 0 0
13 15 3 14 9 19 3
8
0 0 0 0 0 0 0 1
0 0 0 1 0 0 1 0
0 0 0 1 1 0 1 0
0 1 1 0 0 0 0 0
0 0 1 0 0 1 0 0
0 0 0 0 1 0 1 0
0 1 1 0 0 1 0 1
1 0 0 0 0 0 1 0
5 6 20 9 3 17 17 14
8
0 0 0 1 0 1 1 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 1 0
1 0 0 0 1 0 0 0
0 0 0 1 0 0 0 1
1 0 0 0 0 0 0 0
1 1 1 0 0 0 0 1
0 0 0 0 1 0 1 0
12 4 6 16 3 15 13 7

1 9
#2 0
#3 31
#4 1
#5 0
#6 10
#7 0
#8 2
#9 7
#10 10

"""