# 동철이의 프로그래밍 대회!
T = int(input())                        # 몇번 입력 받을지 T로 값 받기   
for i in range(T):                      # T 만큼 for문 시행
    N, M = map(int,input().split())     # N: 사람 명수, M: 문제 개수, 인데 M은 안써도 문제가 풀린다.
    result_count = []                   # 카운팅을 저장할 임시 공간을 작성
    for case in range(N):               # 사람 명수만큼 반복문 시행
        result_count += [sum(map(int,input().split()))]     # 앞서 받았던 사람 명수만큼 값을 input으로 받고, 여기에서 바로 sum 시행하여 사람별 맞은 개수 도출
    max_solv = max(result_count)                            # max를 활용하여 이중 가장 많이 맞은 개수를 구함. 최다 득점자의 수는 count로 최대치를 찾아서 도출
    
    # f스트랭을 활용하여, # + 케이스 순번, 가장 높은 점수를 맞은 사람의 수, 가장 높은 정답 개수를 출력
    print(f'{i+1}# {result_count.count(max_solv)} {max_solv}')