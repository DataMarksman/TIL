# BOJ.20922. 겹치는건 싫어
# 설계 의도: 딕셔너리 활용
# 1. 각 숫자를 리스트로 받아서 for문으로 돕니다.
# 2. 각 숫자가 처음 등장할 경우, dict에 해당 key를 만들어주고 현재 idx를 배정합니다.
# 3. 이미 해당 숫자가 key로 존재한다면, 현재 위치를 딕셔너리 Value list에 추가해줍니다.
# 4. 이렇게 추가해 줄 때, 해당 list의 길이가 K를 넘는다면, 그 리스트의 가장 앞 idx를 뽑아옵니다.
# 5. 이렇게 뽑아온 idx + 1(지운 것 다음 위치) 부터 현재 idx 까지의 길이가 +1(현재 위치 포함) 전체 길이가 된다.
# 6. 이 값을 ans와 비교해서 갱신해준다.
# 개선점:
# python3 기준 296 ms 인데, 조금 더 효율화 가능하지 않을까 싶은 마음이 듭니다.

N, K = map(int, input().split())
num_list = list(map(int, input().split()))
ans = 0
start = 0
check_dict = {0: [], }
for checking in range(N):
    numb = num_list[checking]
    if numb in check_dict:
        check_dict[numb].append(checking)
        if len(check_dict[numb]) > K:
            diff = check_dict[numb].pop(0)
            if diff + 1 > start:
                start = diff + 1
    else:
        check_dict[numb] = [checking]
    if checking - start + 1 > ans:
        ans = int(checking - start) + 1
print(ans)