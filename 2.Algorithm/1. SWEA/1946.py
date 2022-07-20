# 이 문제의 요점은 즉 특정한 규칙으로 정리되어있는 자료들을 원래의 상태로 나열하는 것.
case_count = int(input()) # 처음에 주어지는 케이스의 수는, 압축된 자료의 개수

for i in range(1,case_count + 1): # 이하의 루틴을 주어진 케이스의 수만큼 반복 출력
    case_num = int(input()) # 그 다음에 각 자료별로 주어지는 케이스의 수를 제시함
    stocks = ''
    for j in range(case_num):  # 그 내용을 출력 규격에 맞게 출력하기.
        text, num = input().split()
        stocks += text*int(num)
    print('#'+str(i))
    for k in range(0,len(stocks),10): 
        print(stocks[k:k+10])