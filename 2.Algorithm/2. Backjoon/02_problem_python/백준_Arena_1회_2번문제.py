# BOJ.
# 설계 의도: 조건에 맞는 실행
# 개선점:
import sys
# sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip('\r\n')
N = int(input())
lime_flag = False
start_word = ""
end_word = ""
before_word = ""
visited = set()
for limes in range(N):
    lime = input()
    visited.add(lime)
    if lime == "?":
        if before_word == "":
            start_word = ""
        else:
            start_word = before_word[-1]
        lime_flag = True
    else:
        if lime_flag:
            end_word = lime[0]
            lime_flag = False
        before_word = str(lime)
T = int(input())
if T == 1:
    answer = input()
else:
    answer = ""
    for get_word in range(T):
        word = input()
        if word not in visited:
            if start_word == "" and end_word == "":
                answer = word
            elif start_word == "":
                if word[-1] == end_word:
                    answer = word
            elif end_word == "":
                if word[0] == start_word:
                    answer = word
            else:
                if word[-1] == end_word and word[0] == start_word:
                    answer = word
print(answer)


