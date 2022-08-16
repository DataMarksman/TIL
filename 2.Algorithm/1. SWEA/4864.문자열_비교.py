# 4864. 문자열 비교
for tc in range(int(input())): A=input();B=input();print(f'#{tc+1} {1 if B.find(A) > 0 else 0}')
