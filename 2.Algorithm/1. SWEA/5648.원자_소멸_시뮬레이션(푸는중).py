# 5648. 원자 소멸 시뮬레이션
# 쉽게 생각하자. 
# 이전에 코드 짜놨던거 다 날아가서 약간 빡친 상태로 작성 시작

# 요컨데, 겹치면 죽는다.
# 1. 이전 좌표들의 셋과 이번 시행 좌표들의 셋 개수가 다르면? 중복되는 좌표에 있는걸 터뜨리자.
# 2. 2차원 배열로 놓고 자기가 진행하는 반대 방향에서 
# 저장 형식 예시: dict_A = ({'rocation': (500,100),'move':1,'energy':10},{'rocation': (500,100),'move':0,'energy':10})

T = int(input())
for case_num in range(1,T+1):
    atom_count = int(input())
    dict_Atom = dict()
    for atoms in range(atom_count):
        A, B, C, D = map(int,input().split())
        dict_Atom.append({'rocation': [A, B],'move':C,'energy':D})
    bomb_count = len(dict_Atom)
    for turn in range(2000):
        for atom in dict_Atom:
            if atom['move'] == 0 and dict_Atom.get(atom['rocation']+ (0,1)):
                atom['rocation'][0] 
                += (0,1)
            elif atom['move'] == 1:
                atom['rocation'] += (0,-1)
            elif atom['move'] == 2:
                atom['rocation'] += (-1,0)
            elif atom['move'] == 3:
                atom['rocation'] += (1,0)            
        
        
        
        
        for atom in dict_Atom:
            if atom['move'] == 0:                  # up
                atom['rocation'][0] -= 1 
            elif atom['move'] == 1:
                atom['rocation'][0] += 1
            elif atom['move'] == 2:
                atom['rocation'][1] -= 1
            elif atom['move'] == 3:
                atom['rocation'][1] += 1
        roc_list = dict_Atom.values('rocation')
        