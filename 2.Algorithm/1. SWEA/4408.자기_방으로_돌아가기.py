# 4408. 자기방으로 돌아가기
# 설계: 자료 구조를 잘 인지해야한다.
# 1. 시작 위치보다 작은 수의 방으로도 갈 수 있고,
# 2. 홀수 방과 짝수 방이 같은 복도를 공유한다. (중요! 이거 몰라서 계속 틀림)
# 개선점:
# 1. 문제의 조건을 잘 읽어보지 않으면 왜 틀렸는지, 맞았는지 모른다. 주의하자.

T = int(input())
for case_num in range(1,T+1):
    N = int(input())
    hall = [0] * 201
    student_list = [list(map(int, input().split())) for _ in range(N)]
    for student in range(len(student_list)):
        x = (student_list[student][0]+1)//2
        y = (student_list[student][1]+1)//2
        if y >= x:
            for passing in range(x, y+1):
                hall[passing] += 1
        elif x > y:
            for passing in range(y, x+1):
                hall[passing] += 1
    ans = max(hall)
    print(f'#{case_num} {ans}')
