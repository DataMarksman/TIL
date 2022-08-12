# 프로그래머스 숫자 문자열과 영단어
# https://school.programmers.co.kr/learn/courses/30/lessons/81301?language=python3
# ver1 brute force 방법이 가장 빠름. 생각할 필요가 없다.
def solution(s):
    word = list(str(s+'*********'))
    changed_word = str()
    for alp in range(len(word)):
        if word[alp] == 'z' and word[alp+1] == 'e' and word[alp+2] == 'r' and word[alp+3] == 'o':
            changed_word += '0'
        elif word[alp] == 'o' and word[alp+1] == 'n' and word[alp+2] == 'e':
            changed_word += '1'
        elif word[alp] == 't' and word[alp+1] == 'w' and word[alp+2] == 'o':
            changed_word += '2'
        elif word[alp] == 't' and word[alp+1] == 'h' and word[alp+2] == 'r' and word[alp+3] == 'e' and word[alp+4] == 'e':
            changed_word += '3'
        elif word[alp] == 'f' and word[alp+1] == 'o' and word[alp+2] == 'u' and word[alp+3] == 'r':
            changed_word += '4'
        elif word[alp] == 'f' and word[alp+1] == 'i' and word[alp+2] == 'v' and word[alp+3] == 'e':
            changed_word += '5'
        elif word[alp] == 's' and word[alp+1] == 'i' and word[alp+2] == 'x':
            changed_word += '6'
        elif word[alp] == 's' and word[alp+1] == 'e' and word[alp+2] == 'v' and word[alp+3] == 'e' and word[alp+4] == 'n':
            changed_word += '7'
        elif word[alp] == 'e' and word[alp+1] == 'i' and word[alp+2] == 'g' and word[alp+3] == 'h' and word[alp+4] == 't':
            changed_word += '8'
        elif word[alp] == 'n' and word[alp+1] == 'i' and word[alp+2] == 'n' and word[alp+3] == 'e':
            changed_word += '9'
        elif word[alp].isnumeric():
            changed_word += word[alp]
    answer = int(changed_word)
    return answer
