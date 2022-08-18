# 4613. 러시아 국기 같은 깃발

T = int(input())
for case_num in range(1,T+1):
    N, M = map(int, input().split())
    color_count = [0, 0, 0] # W B R
    for put_in in range(N):
        checking_words = list(input())
        for words in checking_words:
            if words == 'W':
                color_count[0] += 1
            elif words == 'B':
                color_count[1] += 1
            elif words == 'R':
                color_count[2] += 1
    W = color_count[0]%
    color_count[1]
    color_count[2]