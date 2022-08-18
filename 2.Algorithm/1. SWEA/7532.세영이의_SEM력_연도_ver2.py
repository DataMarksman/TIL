# 7532. 세영이의 SEM력 연도

# ver2. 이왕이면 날짜형으로 풀자!:

def check24(num_24):                 # 24가 Full 값인 날짜 데이터 형식
    while num_24 >= 25:              # 25 이상의 값일 경우
        num_24 -= 24                 # -24 해서 다음 단위로 넘기기
    return num_24

def check29(num_29):                 # 29가 Full인 날짜 데이터 형식 
    while num_29 >= 30:              # 30 이상의 값일 경우
        num_29 -= 29                 # -29 해서 다음 단위로 넘기기
    return num_29

T = int(input())
for case_num in range(1,T+1):
    S, E, M = map(int,input().split())
    K = S                            # K가 우리가 구하는 값,
    while True:                      # 첫값의 의미는 K = 365*0 + S
        K_E = check24(K)             # K를 24가 MAX인 날짜 데이터로 변환
        K_M = check29(K)             # K를 29가 MAX인 날짜 데이터로 변환
        if (K_E == E) and (K_M == M):# 변환한 값이 각각 E, M과 일치하면
            print(f'#{case_num} {K}')# 출력
            break                    # 반복문 종료
        K += 365                     # <반복> K는 365*n + S 이므로 += 365
        # 디버깅용: print(K_E, E, K_M, M)