# 4861. 회문
# 설계:
# 1. 값 받을 때, 회문 여부 탐색하고, 가로 값 못 찾으면 세로 탐색
# 2. zip(리스트) 함수로 2차원 배열 행렬 한번에 바꾸는 스킬이 핵심
# 3. ''.join(문자열 리스트) 함수를 활용한 스킬도 핵심
# 4. A[i:i+K][::-1] 도 핵심 스킬
# 개선점:
# 1. zip 함수로 심층적으로 이해하기.
# 2. 2중 for 문 하나로 전부 커버할 수는 없을까?
T = int(input())
for case_num in range(1, T+1):
    N, M = map(int, input().split())
    N = int(N)
    M = int(M)
    flag = False
    words = []
    ans = str()
    for checking in range(N):
        tmp_word = str(input())
        words += [tmp_word]
        for i in range(N - M + 1):
            if tmp_word[i:i+M] == tmp_word[i:i+M][::-1]:
                ans = tmp_word[i:i+M]
                flag = True
    if flag:
        print(f'#{case_num} {ans}')
    else:
        col_words = list(map(list, zip(*words)))
        for re_check in range(N):
            tmp_word = ''.join(col_words[re_check])
            for j in range(N - M + 1):
                if tmp_word[j:j+M] == tmp_word[j:j+M][::-1]:
                    ans = tmp_word[j:j+M]
                    print(f'#{case_num} {ans}')
                    break

