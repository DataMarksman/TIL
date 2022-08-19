# 5356. 의석이의 세로로 말해요

T = int(input())
for case_num in range(1, T+1):
    words_list = [list(input()) for _ in range(5)]
    ans = []
    for i in range(5):
        words_list[i] += '*'*15
    cross_words = list(map(list, zip(*words_list)))
    ans = ''
    for j in range(15):
        ans += ''.join(cross_words[j])
    print(f'#{case_num}', ans.replace('*', ''))
