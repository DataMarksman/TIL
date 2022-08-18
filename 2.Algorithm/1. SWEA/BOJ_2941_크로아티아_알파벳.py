# BOJ 2941 크로아티아 알파벳
word = list(str(input()))
cro_count = len(word)
for i in range(len(word)):
    if word[i] == 'c' and word[i+1] == '=':
        cro_count -= 1
    elif word[i] == 'c' and word[i+1] == '-':
        cro_count -= 1
    elif word[i] == 'd' and word[i+1] == 'z' and word[i + 2] == '=':
        cro_count -= 1
    elif word[i] == 'd' and word[i+1] == '-':
        cro_count -= 1
    elif word[i] == 'l' and word[i+1] == 'j':
        cro_count -= 1
    elif word[i] == 'n' and word[i+1] == 'j':
        cro_count -= 1
    elif word[i] == 's' and word[i+1] == '=':
        cro_count -= 1
    elif word[i] == 'z' and word[i+1] == '=':
        cro_count -= 1
print(cro_count)
