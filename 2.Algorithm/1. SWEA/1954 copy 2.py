case_count = int(1)
num = int(input())
snail_list = [[0]*num]*num    # 0으로 이루어진 num x num의 2차원 배열 생성
print('#',str(case_count))
t = int(0)
start_num = int(1)
while t <= num-2*t:
    for i in range(num-2*t):
        [snail_list[i+t][t]] = return([start_num + i] if snail_list[i+t][t] == int(0) else pass)
        [snail_list[(num-2*t)-1][i+t]] = [start_num + i + ((num-1)-2*t)] if [snail_list[(num-2*t)-1][i+t]] == 0 else pass
        [snail_list[(num-2*t)-1-i][num-1-t]] = [start_num + i + (2*(num-1)-2*t)] if  [snail_list[(num-2*t)-1-i][num-1-t]] == 0 else pass
        [snail_list[t][(num-t)-1-i]] = [start_num + i + (3*(num-1)-2*t)] if [snail_list[t][(num-t)-1-i]] == 0 else pass
        start_num += 4*((num-1)-(2*t))
    else:
        t += 1
case_count += 1
print(snail_list)