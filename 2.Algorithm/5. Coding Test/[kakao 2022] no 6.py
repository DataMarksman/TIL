import sys

sys.setrecursionlimit(10 ** 8)

dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
alpha = ['d', 'l', 'r', 'u']
ans_string = ''
visited_set = [set() for _ in range(2500)]


def solution(n, m, x, y, r, c, k):
    start = (x - 1, y - 1)
    end = (r - 1, c - 1)

    def dfs(idx, words, top):
        global ans_string
        global visited_set
        if ans_string:
            return
        else:
            if top == k - 1:
                X = idx[0]
                Y = idx[1]
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]
                    if (PX, PY) == end:
                        ans_string = words + alpha[direction]
                        return
            else:
                X = idx[0]
                Y = idx[1]
                for direction in range(4):
                    PX = X + dx[direction]
                    PY = Y + dy[direction]
                    if 0 <= PX < n and 0 <= PY < m and (PX, PY) not in visited_set[top]:
                        dfs((PX, PY), words + alpha[direction], top + 1)
                        visited_set[top].add((PX, PY))

    dfs(start, '', 0)
    if ans_string:
        answer = ans_string
    else:
        answer = 'impossible'
    return answer