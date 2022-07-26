case_count = int(1)
num = int(input())
print('#',str(case_count))
snail_list = [[0]*num for j in range(num)]
start_num = int(1)
t = int(0)
for t in range(num-2*t):
    for i in range(num-2*t):
        if snail_list[i+t][t] == 0:
            snail_list[i+t][t] = start_num + i
        if snail_list[(num-2*t)-1][i+t] == 0:
            snail_list[(num-2*t)-1][i+t] = start_num + i + ((num-1)-2*t)
        if snail_list[(num-2*t)-1-i][num-1-t] == 0:
            snail_list[(num-2*t)-1-i][num-1-t] = start_num + i + (2*(num-1)-2*t)
        if snail_list[t][(num-t)-1-i] == 0:
            snail_list[t][(num-t)-1-i] = start_num + i + (3*(num-1)-2*t)
        start_num += 4*((num-1)-(2*t))
case_count += 1
print(snail_list)