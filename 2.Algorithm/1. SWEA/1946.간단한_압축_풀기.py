# 이 문제의 요점은 즉 특정한 규칙으로 정리되어있는 자료들을 원래의 상태로 나열하는 것.

# 처음에 주어지는 input 값은, 압축된 자료의 개수
case_count = int(input()) 

# 이하의 루틴을 자료의 수만큼 반복 출력
for i in range(1,case_count + 1): 

    # 그 다음에 각 자료별로 주어지는 케이스의 수를 제시함 + 스톡 저장을 위한 빈공간 설계
    case_num = int(input()) 
    stocks = ''

    # 그 내용을 출력 규격에 맞게 스톡에 저장
    for j in range(case_num):
        text, num = input().split()
        stocks += text*int(num)
    
    # 현재 자료의 순번을 출력하고
    print('#'+str(i))

    # 10줄씩 잘라서 스톡에 저장된 내용을 출력
    for k in range(0,len(stocks),10): 
        print(stocks[k:k+10])