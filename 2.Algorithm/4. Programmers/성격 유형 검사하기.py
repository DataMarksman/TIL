# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

def solution(survey, choices):
    character_dict = {'R': (0, 0), 'T': (0, 1),
                      'C': (1, 0), 'F': (1, 1),
                      'J': (2, 0), 'M': (2, 1),
                      'A': (3, 0), 'N': (3, 1)}
    character_list = [[0, 0], [0, 0], [0, 0], [0, 0]]
    character_matching = ['RT', 'CF', 'JM', 'AN']
    length = len(survey)
    for check in range(length):
        first = survey[check][0]
        second = survey[check][1]
        if choices[check] >= 5:
            x = character_dict[second][0]
            y = character_dict[second][1]
            character_list[x][y] += choices[check] - 4
        elif choices[check] <= 3:
            x = character_dict[first][0]
            y = character_dict[first][1]
            character_list[x][y] += 4 - choices[check]
    print(character_list)
    answer = ''
    for enter in range(4):
        if character_list[enter][0] >= character_list[enter][1]:
            answer += character_matching[enter][0]
        else:
            answer += character_matching[enter][1]
    return answer