case = int(input())

for i in range(case):
    num = int(input())
    line = list(map(int,input().split()))
    ans = sum(1 for i in line if i <= (sum(line)/len(line)))
    print(f'#{i+1} {ans}')
