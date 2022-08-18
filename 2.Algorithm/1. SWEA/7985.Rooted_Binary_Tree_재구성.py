# Rooted Binary Tree
# ver1: 각 좌표를 뽑아서 해당 좌표에서 아래층으로 내려올 때,
# 해당 좌표에서 2**(n) 만큼 더하거나 빼주면서 내려오는 좌표값을 기준으로 계산.



# ???: 값, [ ] : 위치 좌표 데이터
# 최상위층: (좌표상 정중앙에 위치)             ??? [ 2**(K-2)//2 ]
# -> 아래로 뻗음                          /                        \ 
# 최상위 바로 아래층:  ??? [ (2**(K-2)//2) - (2**(K-j-1)) ]   ???  [ (2**(K-2)//2) + 2**(K-j-1) ]
# 이렇게 내려오는 식의 트리를 최상위 층 부터 구축해 나아가는 방식으로 코드를 작성함.



# 케이스 개수를 T로 받아요!
T = int(input())

# T 만큼 반복해요!
for i in range(T):
    
    # 이번 케이스의 층 수
    K = int(input())
    
    # 각 층의 좌표에 들어갈 값들 map으로 받기
    input_list = list(map(int,input().split()))
    
    # Position, 즉 좌표를 저장해 둘 장소와, 임시 리스트 생성
    po_list = []
    tmp_list = []
    
    # 일단 첫번째 프린트로 케이스 번호와 가장 고레벨 값(중앙 값) 출력
    print(f'#{i+1} {input_list[int((2**K-2)//2)]}')
    
    # 이번 케이스의 층을 쌓아올리는 for 반복문
    for j in range(K):
        
        # j가 0일때, 즉 가장 위층은 이미 나왔으므로 패스하되, 중앙 좌표만 입력
        if j == 0:
            po_list = [int((2**K-2)//2)]
            
        # 임시 리스트를 비워주고, 좌표 리스트 값을 임시 리스트에 넣어줌
        else:
            tmp_list = []
            po_list, tmp_list = tmp_list, po_list
            
            # 임시 리스트에서 받아온 좌표 값에 2의 (지금 내려온 층수)승 만큼 더한 값과 빼준 값 넣기
            for tmp in tmp_list:
                po_list += [tmp-2**(K-j-1),tmp+2**(K-j-1)]
                
            # 출력할 임시 리스트 배정
            answer_list = []
            
            # 뽑아놨던 좌표 리스트에서 좌표를 받아서 각 좌표의 값을 출력
            for position in po_list:
                answer_list += [input_list[position]]
                
            # 이번 층의 각 좌표별 수치를 출력
            print(answer_list)