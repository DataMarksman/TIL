# Rooted Binary Tree
# ver2: 2**(n) 번 만큼 뛰어 넘어가면서 값을 출력하자
# 단, 이미 뽑았던 좌표는 패스 하고 뽑아나가자.
# K가 임의의 값 N으로 주어지면, 최상위층의 리스트 내의 좌표값은 List[(2**N)-1] 이다.

# 이를 풀어서 말하면 2의 N승번째의 위치에 최상층 값이 온다.
# 아래층으로 내려오면서 2의 (N-1)승의 값 만큼 위치 값에서 더하고/빼준 값으로 내려온다.
# 예를 들어, 만약 첫 층에서 8번째에 위치했다면 그 다음에는 4번째와 12번째, 즉 +4, -4의 위치 값이 나온다.

# 이를 통해 (2**k)-1 만큼 점프하면서 지나간 자리를 마킹하고,
# 마킹한 자리 외에 새롭게 밟는 자리를 해당 층에서 출력하는 방식으로 답을 구하고자 한다.

T = int(input())

for i in range(T):
    K = int(input())
    input_list = list(map(int,input().split()))
    for j in range(K):
        print(input_list[::2**(K-j)]) # 일단 여기서 중단. 나중에 다시 적어나아가기.
        # 일단 출력을 보는 용도고, 실제로는 해당 값 쓴 다음에 해당 자리에 0으로 채워넣고,
        # 조건문으로 0의 값을 가지는 자리는 제외하고 출력하도록 하면,
        # 나중에 2**0 즉, 1의 값을 가지고 앞에서부터 전부 출력할때, 이미 나온 것들은 0이 되어 사라지고 그 외의 값들 도출 됩니다.
        # 이 부분 0으로 바꾸고 조건문 걸지 않고서 해결하는 방법을 고심 중.