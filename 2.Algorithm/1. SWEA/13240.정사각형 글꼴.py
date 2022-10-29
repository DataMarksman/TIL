# SWEA. 13240. 정사각형 글꼴
# 설계 목적:
# 1. 일단 들어갈 글자의 순서를 바꾸면 안된다.
# 2. 최적의 수부터 하나씩 줄여나가면서 끼워 맞춰보자.
# 개선점:
# 1. 느리다. 커팅 가능하도록 백트 넣어야 한다.

T = int(input())
for case_num in range(1, T + 1):
    ans = 0
    height, wide, N = map(int, input().split())

    # 만약 N이 0이면 0을 출력해주자.
    if N == 0:
        print(f'#{case_num} {ans}')

    # 그 외에 값이 하나라도 0이 있으면 커트해주자.
    elif height*wide == 0:
        text = list(input().split())
        print(f'#{case_num} {ans}')

    # 이제 본격적인 로직에 들어간다.
    else:
        length_list = list(map(len, input().split()))

        # 확인용 최대값 추출
        max_length = max(length_list)

        # 최대 길이가 넓이 보다 크면 짜른다.
        if max_length > wide:
            print(f'#{case_num} {ans}')

        # 그렇지 않으면 메인 로직 진출
        else:
            # 최적의 수는 가로 기준으로, 가장 긴 놈으로 나눈 몫 만큼 배수 하는 것이다.
            best = wide//max_length

            while best > 0:
                idx = 0
                counting = 1
                stack = length_list[idx]
                idx += 1
                while idx < N and counting < height:
                    if stack + length_list[idx] + 1 <= (wide/best):
                        stack += length_list[idx] + 1
                        idx += 1
                    else:
                        stack = length_list[idx]
                        counting += 1
                        idx += 1
                if counting*best <= height:
                    ans = best
                    break

                # 이번 순회에서 못 찾았으면 -1 해서 다음 루틴 들어가자.
                else:
                    best -= 1
        print(f'#{case_num} {ans}')


