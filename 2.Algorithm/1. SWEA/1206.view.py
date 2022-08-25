# swea 1226. view (초기 풀이)
# diff로 차이를 축적& 탐색하며 동시에 ans에 +1씩 축적
# 밟고 있는 빌딩에서 한칸씩 내려오면서 탐색한다는 논리.

T = 10
for case_num in range(T):
    Num = int(input())
    Building = list(map(int,input().split()))
    ans = 0

# 내가 밟고 있는 빌딩이 앞뒤 2칸보다 높을 경우, 조건문 진입
    for i in range(2,Num):
        if Building[i] > Building[i-1] and Building[i] > Building[i-2]\
                and Building[i] > Building[i+1] and Building[i] > Building[i+2]:

            diff = 0
            while Building[i] - diff != Building[i-1] and Building[i] - diff != Building[i-2] \
                    and Building[i] - diff != Building[i+1] and Building[i] - diff != Building[i+2]:
                diff += 1
                ans += 1
    print(f'#{case_num+1} {ans}')
