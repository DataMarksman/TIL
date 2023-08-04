# BOJ. 2457. 공주님의 정원
# 설계 의도: idx 좌표에 끝 좌표 넣고 슬라이싱 -> MAX값으로 빼기
# 결국 275일동안 피어있으면 되는건데...

# 0. 값 받을때, 시작 위치랑 끝 좌표 최저/최대 조정해주기
# 1. flower_list의 idx = start 포인트
# 2. flower_list[idx]의 값 =  해당 포인트 부터 이어지는 좌표의 끝값
# 3. 값 넣어줄 때부터, 좌표 이전값이랑 비교해서 커트 가능.
# 4. 시작점 (60) 부터, 해당 시작지점에 그어진 끝지점 까지 슬라이싱해서 최대값 뽑아내기
# 5. 이전 트라이에서의 End 값 + 1 에서부터 이전 트라이에서 뽑아온 최대값 까지 슬라이싱 해서 최대값
# 6. 이상을 반복해서 끝 점인 335 도착하면 끝

# 개선점:
# 0. 존나 깎았습니다.
import sys
month_count = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
flower_list = [0]*366
N = int(sys.stdin.readline())
for case_num in range(1, N+1):
    line = list(map(int, sys.stdin.readline().split()))
    A = month_count[line[0]] + line[1]
    B = month_count[line[2]] + line[3]
    if A > 334 or B < 59:
        continue
    else:
        if A <= 59:
            A = 60
        if B >= 336:
            B = 335
        if B > flower_list[A]:
            flower_list[A] = B
flag = True
count = 1
start = 60
end = flower_list[60]
if end >= 335:
    flag = False
while count < N and flag:
    max_idx = max(flower_list[start: end+1])
    if max_idx >= 335:
        count += 1
        flag = False
        break
    start = int(end)
    end = int(max_idx)
    count += 1
if flag:
    print(0)
else:
    print(count)
