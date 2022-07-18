case_count = int(input())

for i in range(1,case_count + 1): 
    case_num = int(input()) 
    stocks = ''
    for j in range(case_num):  
        text, num = input().split()
        stocks += text*int(num)
    print('#'+str(i))
    for k in range(0,len(stocks),10): 
        print(stocks[k:k+10])