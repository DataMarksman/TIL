# 3141. 가장 빠른 문자열 타이밍

for case_num in range(int(input())):
    word = list(map(str, input().split()))
    print(f'#{case_num+1} {len(word[0].replace(word[1], "*"))}')
