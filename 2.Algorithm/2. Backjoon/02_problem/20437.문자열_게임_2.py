# BOJ. 20437 문자열 게임
# 설계 의도: 딕셔너리 연습해보자
# 0. 처음에는 ord() 함수 이용해볼까 하다가, dict가 훨씬 빠를 것 같아서 사용했슴다.
# 0. 그 dict도 if 문으로 분기해서 <'a' in base_dict> 여부에 따라 새로 key 만들어줄까 하다가 그냥 26개 만들었슴다
# 1. 우선 알파벳 소문자 26개 분량을 전부 dict 했으므로, 스트링 각 부분을 읽어서 dict에 해당 알파벳 등장 idx를 기입합니다.
# 2. 이렇게 기입된 알파벳의 개수가 제시된 K를 넘어가면 현재 입력된 알파벳의 idx에서 해당 dict의 K 만큼 뒤에있는 idx를 빼줍니다.
#    -> 쉽게 말해서, 해당 알파벳이 요구 횟수 이상 등장했으면, 요구 횟수만큼의 길이를 가지는 문자열의 길이를 바로 빼줍니다.
# 3. 해당 문자열의 길이가 가장 짧은 문자열이나 가장 긴 문자열과 비교하여 max, min 값을 대체한다.
# 개선점:
# 1. 그때 그때 딕셔너리 제작하는거보다 이게 빨라욧! 아무튼 빠름...
T = int(input())
for case_num in range(1, T+1):
    basic_dict = {'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], 'h': [], 'i': [], 'j': [],
                  'k': [], 'l': [], 'm': [], 'n': [], 'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [],
                  'u': [], 'v': [], 'w': [], 'x': [], 'y': [], 'z': []}
    str_list = input()
    K = int(input())
    flag_min = False
    flag_max = False
    min_length = 9999999999999999999
    max_length = 0
    for checking in range(len(str_list)):
        basic_dict[str_list[checking]] += [checking]
        length_idx = len(basic_dict[str_list[checking]])
        if length_idx >= K:
            D = (basic_dict[str_list[checking]][length_idx-1] - basic_dict[str_list[checking]][length_idx-K]) +1
            if D > max_length:
                max_length = int(D)
                flag_max = True
            if D < min_length:
                min_length = int(D)
                flag_min = True
    if flag_max and flag_min:
        print(f'{min_length} {max_length}')
    else:
        print(-1)



# T = int(input())
# for case_num in range(1, T+1):
#     str_list = input()
#     K = int(input())
#     count_list = [0]*26
#     start_idx = [0]*26
#     min_length = 99999999999
#     min_length_idx = tuple()
#     max_length = 0
#     for checking in range(len(str_list)):
#         ABC = ord(str_list[checking]) - 97
#         if count_list[ABC] == 0:
#             start_idx[ABC] = checking
#         count_list[ABC] += 1
#
#         length = checking - start_idx[ABC] + 1
#         if count_list[ABC] == K:
#             if min_length > length:
#                 min_length = length
#
#                 min_length_idx = (start_idx[ABC], checking)

