# BOJ.
# 설계 의도: 재귀로 푸는 조건부 범위 합
# 0. 재귀 함수로 풀기. 길이가 1, 2, 3이상 일 때를 분리해서 고려하자.
# 1. 모든 재귀에서는 시작과 동시에 전체 수에서 홀수 개수 세어준 뒤에 진행.
# 2. 3 이상일 때는 for문 두개 돌려서 3등분 한 뒤에 그거 더해주고 재귀
# 3. 2 일 때는 숫자 두개 합치고 돌리기
# 4. 1 일 때는 숫자 한개니까 그냥 확인 후 min 값과 max 값 비교해서 최종값 후보 도출
# 개선점:
# 1. A = ''.join(numb[:i]) 졸려서 그런지, 이걸 join이 아니라 더하기로 풀고 있었다. 고쳐서 다행
# 2. range(1, K-1): ... range(i+1, K): 범위를 잘 생각하자. K-2로 주면 K-3까지만 가능해진다.


def cutting(origin, odd_count):
    global min_ans
    global max_ans
    numb = list(str(int(origin)))
    K = len(numb)
    if K == 1:
        if int(origin) % 2 == 1:
            odd_count += 1
        if odd_count > max_ans:
            max_ans = int(odd_count)
        if min_ans > odd_count:
            min_ans = int(odd_count)

    elif K == 2:
        for checking in range(2):
            if int(numb[checking]) % 2 == 1:
                odd_count += 1
        cutting(str(int(numb[0])+int(numb[1])), odd_count)

    else:
        for checking in range(K):
            if int(numb[checking]) % 2 == 1:
                odd_count += 1

        for i in range(1, K-1):
            for j in range(i+1, K):
                A = ''.join(numb[:i])
                B = ''.join(numb[i:j])
                C = ''.join(numb[j:])
                D = int(A) + int(B) + int(C)
                cutting(str(D), odd_count)


min_ans = 9999999999999999999999
max_ans = 0
N = int(input())
cutting(str(N), 0)
print(min_ans, max_ans)
