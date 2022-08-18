# BOJ 17249 태보태보 총난타
punch_line = list(str(input()))
count = 0
left = 0
right = 0
for i in range(len(punch_line)):
    if punch_line[i] == '@':
        count += 1
    elif punch_line[i] == '0':
        left = int(count) + 0
        count = 0
else:
    right = count
print(left, right)