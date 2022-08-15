# 3141. 가장 빠른 문자열 타이밍 (한줄 코딩)
for tc in range(int(input())): A = list(map(str, input().split())); print(f'#{tc+1} {len(A[0].replace(A[1],"*"))}')
