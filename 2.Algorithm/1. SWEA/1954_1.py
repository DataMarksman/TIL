case_count = int(1)

num = int(input())

snail_list = [[0]*num for j in range(num)]
digit = int(1)
print('#',str(case_count))
t = int(0)
while t <= num-2*t:
    for i in range(num-2*t):
        if snail_list[i+t][t] != [0]:
            snail_list[i+t][t] = digit
            digit += 1
    for j in range(num-2*t):
        if snail_list[(num-2*t)-1][j+t] != [0]:
            snail_list[(num-2*t)-1][j+t] = digit
            digit += 1
    for p in range(num-2*t):
        if snail_list[(num-2*t)-1-p][num-1-t] != [0]:
            snail_list[(num-2*t)-1-p][num-1-t] = digit 
            digit += 1
    for q in range(num-2*t):
        if snail_list[t][(num-t)-1-q] != [0]:
            snail_list[t][(num-t)-1-q] = digit
            digit += 1
    else:
        t += 1
case_count += 1
print(snail_list)