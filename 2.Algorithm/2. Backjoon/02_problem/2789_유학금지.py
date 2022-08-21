# BOJ 2789 유학금지
cut_list = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = list(str(input()))
cut_word = str()
for i in range(len(word)):
    if word[i] in cut_list:
        pass
    else:
        cut_word += word[i]
print(cut_word)
