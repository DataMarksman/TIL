# PRG.

# 설계 의도: 조건에 맞는 실행

# 로직의 Main 개념:

# 개선점:

def solution(queries):
    ans_list = ['RR', 'RR', 'Rr', 'Rr', 'rr']

    def find(depth, idx):
        nonlocal answer
        if depth == 1:
            answer.append(ans_list[idx])
            return
        else:
            criteria = 4 ** (depth - 1)
            for quarter in range(1, 5):
                if idx <= criteria * quarter:
                    if quarter == 1:
                        answer.append('RR')
                        return
                    elif quarter == 4:
                        answer.append('rr')
                        return
                    else:
                        return find(depth - 1, idx // 4)

    answer = []
    for check in range(len(queries)):
        find(queries[check][0] - 1, queries[check][1])
    return answer